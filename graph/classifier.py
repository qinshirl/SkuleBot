# from langchain.chat_models import init_chat_model
# from langchain.output_parsers import PydanticOutputParser
# from pydantic import BaseModel, Field
# from graph.state import State
#
# llm = init_chat_model("openai:gpt-4.1")
#
#
# class IntentSchema(BaseModel):
#     intent: str = Field(
#         description="The type of request. Must be one of: topic_lookup, course_lookup, course_list, exam_lookup, emotional, unknown"
#     )
#
# parser = PydanticOutputParser(pydantic_object=IntentSchema)
#
# def classify_intent(state: State) -> dict:
#     last_message = state["messages"][-1]
#
#     prompt = parser.get_format_instructions() + "\n\n" + f"""
# You are an AI assistant helping undergraduate students in the **University of Toronto Faculty of Applied Science & Engineering**.
#
# Your job is to classify the user’s intent based on their message.
#
# Here are the valid intent types:
# - **topic_lookup**: The user is asking about a technical subject (e.g., "concrete curing," "thermodynamics," "TCP/IP") and wants to know which courses cover this topic.
# - **course_lookup**: The user directly mentions a course code (e.g., "Tell me about CIV102" or "What is ECE243?")
# - **course_list**: The user is looking for a list of courses by year, specialization, or program (e.g., "What are the 3rd-year ChemE electives?")
# - **exam_lookup**: The user wants to find past exams, syllabi, or outlines (e.g., "Do you have exams for MIE301?" or "ECE110 syllabus?")
# - **emotional**: The user is overwhelmed, frustrated, confused, or expressing stress about school or courses.
# - **unknown**: The message does not clearly fall into any of the above.
#
# User message:
# {last_message.content}
#
# """
#
#     response = llm.invoke(prompt)
#     parsed = parser.parse(response.content)
#
#     return {"intent": parsed.intent}

from typing import List, Optional, Literal

from langchain.chat_models import init_chat_model
# from langchain.output_parsers import PydanticOutputParser
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel, Field

from graph.state import State

llm = init_chat_model("openai:gpt-4.1")


# Allowed intents stay the same as your original design
IntentType = Literal[
    "topic_lookup",
    "course_lookup",
    "course_list",
    "exam_lookup",
    "emotional",
    "unknown",
]


class IntentSchema(BaseModel):
    intent: IntentType = Field(
        description=(
            "The type of request. Must be one of: "
            "topic_lookup, course_lookup, course_list, exam_lookup, emotional, unknown."
        )
    )

    # course-related queries:
    request_type: Optional[Literal["single_course", "course_list"]] = Field(
        default=None,
        description=(
            "If the user is asking about courses, specify whether it is "
            "'single_course' (one specific course) or 'course_list' (a set/list "
            "of courses). Leave null if not course-related."
        ),
    )

    wants_exams: bool = Field(
        default=False,
        description=(
            "Set to true if the user explicitly or implicitly asks for past exams, "
            "sample questions, midterms, finals, or syllabi/outlines."
        ),
    )

    topic: Optional[str] = Field(
        default=None,
        description="Short phrase summarizing the topic (e.g., 'prereqs', 'workload', 'AI electives').",
    )

    course_codes: Optional[List[str]] = Field(
        default=None,
        description="List of course codes mentioned in the message. Use [] if none.",
    )

    course_query: Optional[str] = Field(
        default=None,
        description=(
            "If the user is describing the kind of courses they want (e.g. "
            "'computer networks', 'AI courses'), summarize that description as a short query."
        ),
    )


parser = PydanticOutputParser(pydantic_object=IntentSchema)


def classify_intent(state: State) -> dict:
    last_message = state["messages"][-1]
    # user_text = getattr(last_message, "content", last_message.get("content"))
    if hasattr(last_message, "content"):
        user_text = last_message.content
    elif isinstance(last_message, dict):
        user_text = last_message.get("content", "")
    else:
        user_text = str(last_message)

    format_instructions = parser.get_format_instructions()

    prompt = f"""
You are an AI assistant helping undergraduate students in the
**University of Toronto Faculty of Applied Science & Engineering**.

Your job is to classify the user’s intent based on their message
and extract some useful structured fields.

Valid *intent* values:
- **topic_lookup**: The user is asking about a technical subject
  (e.g., "concrete curing", "thermodynamics", "TCP/IP") and wants to know
  which courses cover this topic.
- **course_lookup**: The user directly mentions one or more course codes
  (e.g., "Tell me about CIV102", "What is ECE243?").
- **course_list**: The user is looking for a list of courses by year,
  specialization, or program (e.g., "What are the 3rd-year ChemE electives?",
  "courses related to computer networks").
- **exam_lookup**: The user wants past exams, sample questions, syllabi,
  or outlines (e.g., "Do you have exams for MIE301?", "ECE110 syllabus?",
  "give me some sample questions from ECE110").
- **emotional**: The user is overwhelmed, frustrated, confused, or expressing
  stress about school or courses.
- **unknown**: The message does not clearly fall into any of the above.

Additional fields:

- **request_type**:
  - Use "single_course" if the question is mainly about one specific course
    (e.g., "sample questions from ECE110").
  - Use "course_list" if it is about multiple or unspecified courses
    (e.g., "courses related to computer networks and their past exams").
  - Leave null if the query is not course-related.

- **wants_exams**:
  - True if the user is asking for past exams, sample questions, midterms,
    finals, or syllabi/outlines.
  - False otherwise.

- **topic**: A short phrase like "prereqs", "workload", "AI electives",
  "sample questions", "networking courses", etc.

- **course_codes**:
  - Extract all explicit course codes mentioned, e.g. ["ECE110", "CSC207"].
  - If none are mentioned, use [].

- **course_query**:
  - If the user is describing *what kind of courses* they want without
    giving exact codes (e.g., "computer networks", "AI courses for second year"),
    summarize that description here.
  - Otherwise leave null.

Return a single JSON object matching this schema:

{format_instructions}

User message:
\"\"\"{user_text}\"\"\"
"""

    response = llm.invoke(prompt)
    parsed: IntentSchema = parser.parse(response.content)

    return {
        "intent": parsed.intent,
        "request_type": parsed.request_type,
        "wants_exams": parsed.wants_exams,
        "topic": parsed.topic,
        "course_codes": parsed.course_codes,
        "course_query": parsed.course_query,
    }

