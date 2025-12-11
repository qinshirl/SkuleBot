#
# from __future__ import annotations
#
# import re
# from typing import Dict, Any, List
#
# from graph.state import State
#
#
# def _extract_description_from_context(course_code: str, ctx: str) -> str:
#
#     if not ctx:
#         return f"{course_code}: No description found."
#     pattern = re.compile(
#         rf"{course_code}[^.\n]*[.\n]?",
#         flags=re.IGNORECASE
#     )
#     found = pattern.findall(ctx)
#
#     if found:
#         desc = found[0].strip()
#         if len(desc) > 2:
#             return desc
#
#     return f"{course_code}: No specific description found in retrieved materials."
#
#
# async def course_info_node(state: State) -> Dict[str, Any]:
#
#     ctx = state.get("lightrag_context", "") or ""
#     selected = state.get("selected_course")
#     suggested = state.get("suggested_courses") or []
#
#     course_codes: List[str] = []
#
#     if selected:
#         code = selected.get("code")
#         if code:
#             course_codes.append(code)
#
#     for entry in suggested:
#         code = entry.get("code")
#         if code:
#             course_codes.append(code)
#
#     course_codes = list(dict.fromkeys(course_codes))
#
#     if not course_codes:
#         print("[course_info] No course codes found. Skipping.")
#         return {}
#
#     print(f"[course_info] Gathering info for courses: {course_codes}")
#
#     info: Dict[str, Dict[str, Any]] = {}
#
#     for code in course_codes:
#         description = _extract_description_from_context(code, ctx)
#
#         info[code] = {
#             "code": code,
#             "title": code,
#             "description": description,
#             "source": "LightRAG"
#         }
#
#     print("[course_info] Completed multi-course info extraction.")
#
#     return {
#         "course_info": info
#     }


from __future__ import annotations

import re
from typing import Dict, Any, List

from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from graph.state import State


llm = init_chat_model("openai:gpt-4.1")


class SingleCourseInfo(BaseModel):
    code: str = Field(..., description="Course code, e.g., MAT186H1F")
    title: str = Field(
        ...,
        description="Human-readable course title, e.g., 'Calculus I' or 'Calculus II'.",
    )
    summary: str = Field(
        ...,
        description="Short paragraph summarizing what the course is about.",
    )
    key_topics: List[str] = Field(
        default_factory=list,
        description="Bullet list of key topics / concepts covered in the course.",
    )
    assessments: List[str] = Field(
        default_factory=list,
        description="Important assessment info: tests, quizzes, final exam, etc.",
    )
    instructors: List[str] = Field(
        default_factory=list,
        description="Names of instructors or coordinators mentioned, if any.",
    )
    resources: List[str] = Field(
        default_factory=list,
        description="Important resources like textbooks, course website, WeBWorK, etc.",
    )


class MultiCourseInfo(BaseModel):
    courses: List[SingleCourseInfo]


parser = PydanticOutputParser(pydantic_object=MultiCourseInfo)

# fallback option
def _extract_description_from_context(course_code: str, ctx: str) -> str:
    if not ctx:
        return f"{course_code}: No description found."
    pattern = re.compile(
        rf"{re.escape(course_code)}[^.\n]*[.\n]?",
        flags=re.IGNORECASE,
    )
    found = pattern.findall(ctx)

    if found:
        desc = found[0].strip()
        if len(desc) > 2:
            return desc

    return f"{course_code}: No specific description found in retrieved materials."




async def _build_course_info_with_llm(
    course_codes: List[str], ctx: str
) -> Dict[str, Dict[str, Any]]:

    if not course_codes or not ctx:
        return {}

    format_instructions = parser.get_format_instructions()

    prompt = f"""
You are given:
1. A list of **University of Toronto course codes**.
2. A chunk of text which includes:
   - "Knowledge Graph Data (Entity)" lines
   - "Knowledge Graph Data (Relationship)" lines
   - Document chunks (e.g., course info, syllabus, schedule, assessments, etc.)

Your task:
For **each** course code in the list, extract and summarize all relevant information
about that course from the text. Focus on:
- Full / human-readable course title
- What the course is about (1–3 sentence summary)
- Key topics and concepts covered
- Assessments (tests, quizzes, final exam, homework systems like WeBWorK)
- Important instructors / coordinators mentioned
- Key resources (textbook, course website, online tools)

If some fields are not mentioned, leave them empty.

Return the result ONLY in the following format:

{format_instructions}

Course codes:
{course_codes}

Context text (truncated if long):
```text
{ctx[:8000]}
```"""

    ai_msg = await llm.ainvoke(prompt)

    result: Dict[str, Dict[str, Any]] = {}

    try:
        parsed: MultiCourseInfo = parser.parse(ai_msg.content)
        for course in parsed.courses:
            # Normalize the code (remove spaces) to match earlier steps
            code_norm = course.code.replace(" ", "")
            result[code_norm] = {
                "code": code_norm,
                "title": course.title or code_norm,
                "summary": course.summary,
                "key_topics": course.key_topics,
                "assessments": course.assessments,
                "instructors": course.instructors,
                "resources": course.resources,
                "source": "LightRAG+LLM",
            }
    except Exception as e:
        print(f"[course_info] LLM parse error, will rely on regex fallback: {e}")

    return result




async def course_info_node(state: State) -> Dict[str, Any]:
    ctx = state.get("lightrag_context", "") or ""
    selected = state.get("selected_course")
    suggested = state.get("suggested_courses") or []

    course_codes: List[str] = []

    if selected:
        code = selected.get("code")
        if code:
            course_codes.append(code)

    for entry in suggested:
        code = entry.get("code")
        if code:
            course_codes.append(code)

    course_codes = list(dict.fromkeys(course_codes))

    if not course_codes:
        print("[course_info] No course codes found. Skipping.")
        return {}

    print(f"[course_info] Gathering info for courses: {course_codes}")

    info: Dict[str, Dict[str, Any]] = await _build_course_info_with_llm(
        course_codes, ctx
    )

    for code in course_codes:
        norm = code.replace(" ", "")
        if norm not in info:
            desc = _extract_description_from_context(norm, ctx)
            info[norm] = {
                "code": norm,
                "title": norm,
                "summary": desc,
                "key_topics": [],
                "assessments": [],
                "instructors": [],
                "resources": [],
                "source": "LightRAG (regex fallback)",
            }
        else:
            if not info[norm].get("summary"):
                info[norm]["summary"] = _extract_description_from_context(norm, ctx)

    print("[course_info] Completed multi-course info extraction.")

    return {
        "course_info": info
    }
