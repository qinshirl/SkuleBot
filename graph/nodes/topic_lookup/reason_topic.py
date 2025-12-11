# from langchain.chat_models import init_chat_model
# from graph.state import State
#
# llm = init_chat_model("openai:gpt-4.1")
#
# def reason_topic_node(state: State) -> dict:
#     # last_user_message = state["messages"][-1]["content"]
#     last_user_message = state["messages"][-1].content
#
#     prompt = f"""
# You are an AI assistant helping engineering students at the University of Toronto.
#
# A student asked the following question:
#
# "{last_user_message}"
#
# Your task is to identify the **main technical subject area** this question is about.
# Examples of subject areas:
# "Computer Networks", "Control Systems",
# "Thermodynamics", "Fluid Mechanics",
# "Structural Mechanics", "Geotechnical Engineering",
# "Process Control", "Reaction Engineering",
# "Materials Characterization", "Corrosion Science",
# "Mine Ventilation", "Rock Mechanics",
# "Operations Research", "Human Factors Engineering",
# "Machine Learning", "Biomedical Signal Processing", etc.
#
# Just reply with the name of the technical area. Keep it short and broad.
# """
#
#     response = llm.invoke(prompt)
#     inferred_topic = response.content.strip()
#
# ############################################################################
#     print(f"[Reason Topic Node] Inferred topic: {inferred_topic}")
# ############################################################################
#     return {
#         "topic": inferred_topic,
#         "messages": [
#             {"role": "assistant", "content": f"Got it — this seems related to **{inferred_topic}**. Let me find some courses for you."}
#         ]
#     }


from langchain.chat_models import init_chat_model
# from langchain.schema import AIMessage
from langchain_core.messages import HumanMessage, AIMessage

from graph.state import State

llm = init_chat_model("openai:gpt-4.1")


def _infer_topic_from_text(user_text: str) -> str:
    """Optional helper: infer broad technical area if topic is missing."""
    prompt = f"""
You are an AI assistant helping engineering students at the University of Toronto.

A student asked the following question:

\"\"\"{user_text}\"\"\"

Your task is to identify the **main technical subject area** this question is about.
Examples of subject areas:
"Computer Networks", "Control Systems",
"Thermodynamics", "Fluid Mechanics",
"Structural Mechanics", "Geotechnical Engineering",
"Process Control", "Reaction Engineering",
"Materials Characterization", "Corrosion Science",
"Mine Ventilation", "Rock Mechanics",
"Operations Research", "Human Factors Engineering",
"Machine Learning", "Biomedical Signal Processing", etc.

Just reply with the name of the technical area. Keep it short and broad.
"""

    response = llm.invoke(prompt)
    return response.content.strip()


def reason_topic_node(state: State) -> dict:

    last_user_message = state["messages"][-1].content

    intent = state.get("intent")
    request_type = state.get("request_type")
    wants_exams = bool(state.get("wants_exams") or False)
    course_codes = state.get("course_codes") or []
    course_query = state.get("course_query")
    topic = state.get("topic")

    if request_type is None:
        if len(course_codes) == 1:
            request_type = "single_course"
        else:
            request_type = "course_list"

    if topic is None and intent in {"topic_lookup", "course_list"}:
        inferred_topic = _infer_topic_from_text(last_user_message)
        topic = inferred_topic
        if not course_query:
            course_query = inferred_topic
        print(f"[Reason Topic] Inferred topic: {inferred_topic}")
    else:
        print(f"[Reason Topic] Using existing topic: {topic}, request_type: {request_type}, wants_exams: {wants_exams}")


    return {
        "request_type": request_type,
        "wants_exams": wants_exams,
        "topic": topic,
        "course_query": course_query,
    }
