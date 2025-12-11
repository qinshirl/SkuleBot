
from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, START, END
# from langchain.schema import HumanMessage, AIMessage
from langchain_core.messages import HumanMessage, AIMessage

from graph.state import State
from graph.classifier import classify_intent
from graph.router import router

from graph.nodes.topic_lookup import build_topic_lookup_graph
from graph.nodes.human import human_node
from graph.nodes.therapist import therapist_node

# def placeholder_node(state: State) -> dict:
#     return {
#         "messages": state["messages"] + [
#             AIMessage(content="This feature is not implemented yet.")
#         ]
#     }


builder = StateGraph(State)

builder.add_node("classifier", classify_intent)
builder.add_node("router", router)

builder.add_node("topic_lookup", build_topic_lookup_graph())

builder.add_node("therapist", therapist_node)
builder.add_node("human", human_node)

builder.add_edge(START, "classifier")
builder.add_edge("classifier", "router")

builder.add_conditional_edges(
    "router",
    lambda state: state["next"],
    {
        "topic_lookup": "topic_lookup",
        "therapist": "therapist",
        "human": "human",
    },
)

builder.add_edge("topic_lookup", END)
builder.add_edge("therapist", END)
builder.add_edge("human", END)

graph = builder.compile()


def run_chat():
    state: State = {
        "messages": [],

        "intent": None,
        "wants_exams": False,
        "topic": None,
        "course_query": None,

        "selected_course": None,
        "suggested_courses": None,

        "lightrag_context": None,
        "lightrag_references": None,
        "lightrag_raw": None,

        "course_info": None,
        "exam_content": None,
    }

    print("Welcome to SkuleBot! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        state["messages"].append(HumanMessage(content=user_input))

        state = graph.invoke(state)

        if state.get("messages"):
            assistant_reply = state["messages"][-1].content
            print(f"Assistant: {assistant_reply}\n")


if __name__ == "__main__":
    run_chat()
