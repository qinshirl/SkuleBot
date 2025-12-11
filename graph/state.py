# from typing import Annotated, Optional
# from langgraph.graph.message import add_messages
# from typing_extensions import TypedDict
#
#
# class State(TypedDict):
#     messages: Annotated[list, add_messages]
#
#     intent: Optional[str] # type of query
#     topic: Optional[str] # topic
#     suggested_courses: Optional[list[dict]]
#     course_info: Optional[str]
#
#
#
# from typing import Annotated, Optional, List, Dict
# from langgraph.graph.message import add_messages
# from typing_extensions import TypedDict
#
#
# class State(TypedDict):
#     messages: Annotated[list, add_messages]
#     intent: Optional[str]
#     request_type: Optional[str]
#     wants_exams: Optional[bool]
#
#     topic: Optional[str]
#     course_codes: Optional[List[str]]
#
#     course_query: Optional[str]
#
#     selected_course: Optional[Dict]
#     suggested_courses: Optional[List[Dict]]
#     course_info: Optional[Dict]
#     exams_by_course: Optional[Dict[str, List[Dict]]]
#


from typing import Annotated, Optional, List, Dict, Any
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

class State(TypedDict, total=False):

    messages: Annotated[List[Dict[str, Any]], add_messages]
    intent: Optional[str]
    wants_exams: Optional[bool]
    topic: Optional[str]
    course_query: Optional[str]
    selected_course: Optional[Dict]
    suggested_courses: Optional[List[Dict]]

    lightrag_context: Optional[str]
    lightrag_references: Optional[List[Dict]]
    lightrag_raw: Optional[Dict[str, Any]]

    course_info: Optional[Dict[str, Dict[str, Any]]]
    exam_content: Optional[str]

    exams_by_course: Optional[Dict[str, List[Dict]]]

    current_course_code: Optional[str]
    last_course_query: Optional[str]

    pass

