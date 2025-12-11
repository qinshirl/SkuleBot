from langchain_core.messages import HumanMessage
from graph.state import State

from main import graph, create_initial_state

async def skulebot_chat(user_message: str) -> str:
    state: State = create_initial_state()
    state["messages"].append(HumanMessage(content=user_message))

    result_state: State = await graph.ainvoke(state)

    messages = result_state.get("messages", [])
    if not messages:
        return "Hmmmmmmmm :(, I didn't manage to generate a response."

    last = messages[-1]

    return getattr(last, "content", str(last))

