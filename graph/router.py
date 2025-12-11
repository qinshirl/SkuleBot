# from graph.state import State
#
# def router(state: State) -> dict:
#     intent = state.get("intent", "unknown")
# ############################################################################
#     print(f"[Router] Detected intent: {intent}")
# ############################################################################
#     if intent == "topic_lookup":
#         return {"next": "topic_lookup"}
#     elif intent == "course_lookup":
#         return {"next": "course_lookup"}
#     elif intent == "course_list":
#         return {"next": "course_list"}
#     elif intent == "exam_lookup":
#         return {"next": "exam_fetcher"}
#     elif intent == "emotional":
#         return {"next": "therapist"}
#     else:
#         return {"next": "human"}  # unknown or unclear intent fallback



from graph.state import State

COURSE_INTENTS = {
    "topic_lookup",
    "course_lookup",
    "course_list",
    "exam_lookup",
}


def router(state: State) -> dict:
    intent = state.get("intent") or "unknown"
    print(f"[Router] Detected intent: {intent}")

    if intent in COURSE_INTENTS:
        return {"next": "topic_lookup"}

    if intent == "emotional":
        print(f"should go to therapist")
        return {"next": "therapist"}

    return {"next": "human"}
