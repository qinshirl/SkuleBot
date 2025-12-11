# from langgraph.graph import StateGraph, END

# from graph.state import State

# from graph.nodes.topic_lookup.reason_topic import reason_topic_node

# from graph.nodes.topic_lookup.search_courses import search_courses_node

# from graph.nodes.topic_lookup.refine_and_respond import refine_and_respond_node

#

# def build_topic_lookup_graph():

#     # subgraph
# subgraph

#     topic_graph = StateGraph(State)

#

#     topic_graph.add_node("reason_topic", reason_topic_node)

#     topic_graph.add_node("search_courses", search_courses_node)

#     topic_graph.add_node("refine_and_respond", refine_and_respond_node)

#

#     # connect subgraph flow
# connect subgraph flow

#     topic_graph.set_entry_point("reason_topic")

#     topic_graph.add_edge("reason_topic", "search_courses")

#     topic_graph.add_edge("search_courses", "refine_and_respond")

#     topic_graph.add_edge("refine_and_respond", END)

# _

#     return topic_graph.compile()

import asyncio
from langgraph.graph import StateGraph, END

from graph.state import State

from graph.nodes.topic_lookup.reason_topic import reason_topic_node
from graph.nodes.topic_lookup.search_courses import search_courses_node
from graph.nodes.topic_lookup.course_info import course_info_node
from graph.nodes.topic_lookup.exam_fetcher import exam_fetcher_node
from graph.nodes.topic_lookup.refine_and_respond import refine_and_respond_node

def wrap_async(fn):
    """Convert async node → sync node using asyncio.run()."""
    def sync_fn(state: State):
        return asyncio.run(fn(state))
    return sync_fn

def build_topic_lookup_graph():
    topic_graph = StateGraph(State)

    topic_graph.add_node("reason_topic", reason_topic_node)

    topic_graph.add_node("search_courses", wrap_async(search_courses_node))
    topic_graph.add_node("course_info_step", wrap_async(course_info_node))
    topic_graph.add_node("exam_fetcher", wrap_async(exam_fetcher_node))
    topic_graph.add_node("refine_and_respond", wrap_async(refine_and_respond_node))

    topic_graph.set_entry_point("reason_topic")
    topic_graph.add_edge("reason_topic", "search_courses")

    def branch_after_search(state: State) -> str:
        selected = state.get("selected_course")
        suggested = state.get("suggested_courses") or []
        if selected or suggested:
            return "course_info_step"
        return "refine_and_respond"

    topic_graph.add_conditional_edges(
        "search_courses",
        branch_after_search,
        {
            "course_info_step": "course_info_step",
            "refine_and_respond": "refine_and_respond",
        },
    )

    def branch_after_course_info(state: State) -> str:
        if state.get("wants_exams", False):
            return "exam_fetcher"
        return "refine_and_respond"

    topic_graph.add_conditional_edges(
        "course_info_step",
        branch_after_course_info,
        {
            "exam_fetcher": "exam_fetcher",
            "refine_and_respond": "refine_and_respond",
        },
    )

    topic_graph.add_edge("exam_fetcher", "refine_and_respond")
    topic_graph.add_edge("refine_and_respond", END)

    return topic_graph.compile()

