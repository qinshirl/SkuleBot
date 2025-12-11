# # # graph/nodes/topic_lookup/exam_fetcher.py
# #
# # from __future__ import annotations
# #
# # from typing import Dict, Any, List
# #
# # from graph.state import State
# # from .kg_client import run_query
# #
# #
# # def exam_fetcher_node(state: State) -> dict:
# #
# #     wants_exams = bool(state.get("wants_exams"))
# #     if not wants_exams:
# #         print("[exam_fetcher] wants_exams is False – skipping exam lookup.")
# #         return {}
# #
# #     request_type = state.get("request_type") or "course_list"
# #
# #     codes: List[str] = []
# #
# #     if request_type == "single_course":
# #         course = state.get("selected_course") or {}
# #         code = course.get("code")
# #         if code:
# #             codes.append(code)
# #         else:
# #             print("[exam_fetcher] No code in selected_course.")
# #     else:
# #         for c in state.get("suggested_courses") or []:
# #             code = c.get("code")
# #             if code:
# #                 codes.append(code)
# #
# #     # Remove duplicates
# #     codes = sorted(set(codes))
# #     if not codes:
# #         print("[exam_fetcher] No course codes to fetch exams for.")
# #         return {}
# #
# #     print(f"[exam_fetcher] Fetching exams for codes: {codes}")
# #
# #     query = """
# #     MATCH (c:Course)-[:HAS_EXAM]->(e:Exam)
# #     WHERE c.code IN $codes
# #     RETURN c.code AS code, e
# #     ORDER BY e.year DESC, e.term DESC
# #     """
# #     records = run_query(query, {"codes": codes})
# #
# #     exams_by_course: Dict[str, List[Dict[str, Any]]] = {code: [] for code in codes}
# #
# #     for rec in records:
# #         code = rec["code"]
# #         e = dict(rec["e"])
# #         exams_by_course.setdefault(code, []).append(
# #             {
# #                 "year": e.get("year"),
# #                 "term": e.get("term"),
# #                 "type": e.get("type"),
# #                 "url": e.get("url"),
# #                 "hasSolutions": e.get("hasSolutions"),
# #             }
# #         )
# #
# #     print("[exam_fetcher] Retrieved exam counts:", {k: len(v) for k, v in exams_by_course.items()})
# #
# #     return {"exams_by_course": exams_by_course}
# from __future__ import annotations
#
# from typing import Dict, Any
# from graph.state import State
# from langchain_openai import ChatOpenAI
#
#
# llm_instance = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0.2,
# )
#
#
# async def exam_fetcher_node(state: State) -> Dict[str, Any]:
#     """
#     Pure LLM-driven organizer.
#
#     Preconditions:
#         - state["wants_exams"] already set upstream.
#         - LightRAG has already populated:
#             lightrag_context
#             lightrag_references
#             lightrag_raw
#
#     This node:
#         - Does NOT decide whether user wants exams
#         - Does NOT filter by keywords
#         - Does NOT guess filenames
#         - Lets the LLM reorganize ALL retrieved context for exam info
#
#     Output:
#         {
#             "exam_content": <LLM-cleaned exam info>,
#         }
#
#     If no exam content is found, returns empty dict.
#     """
#
#     wants_exams = state.get("wants_exams", False)
#     if not wants_exams:
#         print("[exam_fetcher] wants_exams=False. Skipping.")
#         return {}
#
#     rag_ctx = state.get("lightrag_context", "") or ""
#     rag_refs = state.get("lightrag_references", []) or []
#     rag_raw = state.get("lightrag_raw", {}) or {}
#
#     print("[exam_fetcher] LLM reorganizing exam content...")
#
#     # LLM prompt: reorganizing, extracting, structuring exam info
#     prompt = f"""
# You are an AI assistant specialized in analyzing course materials.
#
# The user explicitly wants **exam / test / quiz** information for this course.
#
# Below is all the retrieved content from LightRAG:
# -------------------------------------
# CONTEXT:
# {rag_ctx}
#
# REFERENCES:
# {rag_refs}
#
# RAW RESULT:
# {rag_raw}
# -------------------------------------
#
# Your task:
# 1. Carefully inspect the content.
# 2. Identify anything related to exams, tests, midterms, finals, quizzes, or assessments.
# 3. Reconstruct these into a **clean, structured, human-readable summary**.
# 4. If possible, include:
#    - known exam types (midterm, final, quiz, etc.)
#    - formats
#    - difficulty notes
#    - dates (if any)
#    - sample topics (if any)
#    - links or filenames (if referenced)
# 5. The output should be useful for a student preparing for an exam.
# 6. If there is no exam information in the content, respond with: "NO_EXAM_INFO".
#
# Return only the cleaned summary.
#     """
#
#     exam_summary = await llm_instance(prompt)
#     exam_summary = exam_summary.strip()
#
#     if exam_summary.upper() == "NO_EXAM_INFO":
#         print("[exam_fetcher] LLM found no exam-related content.")
#         return {"exam_content": None}
#
#     print("[exam_fetcher] Exam content reconstructed by LLM.")
#
#     return {
#         "exam_content": exam_summary
#     }
from __future__ import annotations

from typing import Dict, Any, List, Optional

from graph.state import State
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

llm_instance = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
)


class SingleExam(BaseModel):
    name: str = Field(
        ...,
        description="Name/label, e.g. 'Test 1', 'Midterm', 'Final Exam', 'Quiz 1'."
    )
    type: Optional[str] = Field(
        None,
        description="High-level type: 'midterm', 'final', 'quiz', 'test', etc."
    )
    date: Optional[str] = Field(
        None,
        description="Date or time info if mentioned, e.g. 'Oct 7, 12:15–1:55 PM'."
    )
    coverage: Optional[str] = Field(
        None,
        description="What topics/chapters/sections this exam covers, if stated."
    )
    notes: Optional[str] = Field(
        None,
        description="Other relevant info (format, location, percentage weight, etc.)."
    )
    sample_questions: List[str] = Field(
        default_factory=list,
        description=(
            "A list of exact or near-exact sample exam questions found in the text. "
            "Do NOT invent questions; only include them if they clearly appear."
        ),
    )


class CourseExams(BaseModel):
    course_code: str = Field(..., description="Course code like MAT186H1F, MAT187, ECE110, APS111, APS112 etc.")
    exams: List[SingleExam] = Field(
        default_factory=list,
        description="List of tests/quizzes/exams for this course."
    )


class ExamExtractionResult(BaseModel):

    courses: List[CourseExams] = Field(
        default_factory=list,
        description="Exam info, grouped by course."
    )


exam_parser = PydanticOutputParser(pydantic_object=ExamExtractionResult)


def _collect_course_codes(state: State) -> List[str]:


    codes: List[str] = []

    selected = state.get("selected_course") or {}
    selected_code = selected.get("code")
    if selected_code:
        codes.append(selected_code)

    for c in state.get("suggested_courses") or []:
        code = (c or {}).get("code")
        if code:
            codes.append(code)

    if not codes:
        current = state.get("current_course_code")
        if current:
            codes.append(current)

    seen = set()
    ordered: List[str] = []
    for c in codes:
        if c and c not in seen:
            seen.add(c)
            ordered.append(c)

    return ordered


# def _collect_course_codes(state: State) -> List[str]:
#
#     request_type = state.get("request_type") or "course_list"
#     codes: List[str] = []
#
#     if request_type == "single_course":
#         course = state.get("selected_course") or {}
#         code = course.get("code")
#         if code:
#             codes.append(code)
#     else:
#         for c in state.get("suggested_courses") or []:
#             code = c.get("code")
#             if code:
#                 codes.append(code)
#
#     seen = set()
#     ordered: List[str] = []
#     for c in codes:
#         if c not in seen:
#             seen.add(c)
#             ordered.append(c)
#
#     return ordered

async def _extract_exams_with_llm(
    course_codes: List[str],
    ctx: str,
    refs: Any,
    raw: Any,
) -> Dict[str, List[Dict[str, Any]]]:

    if not course_codes or not ctx:
        return {}

    format_instructions = exam_parser.get_format_instructions()

    prompt = f"""
You are an AI assistant specialized in analyzing university course materials.

The user wants **exam / test / quiz** information, including **sample questions**.

You are given:
1. A list of course codes (University of Toronto style, e.g., MAT186H1F, MAT187).
2. LightRAG output which may include:
   - Knowledge Graph entities and relationships
   - Document chunks from course outlines, syllabi, schedules, or exams.

Your job:
For **each** course code, extract any information related to:
- Exams, tests, midterms, quizzes, final exams
- Dates and times
- Topics/chapters covered
- Other relevant info (format, location, weight, etc.)
- **Sample questions** that clearly appear in the text

Important rules for sample questions:
- Only include questions that are clearly exam-style questions found in the text.
- Copy them as faithfully as possible (you may lightly clean formatting).
- Do **NOT** invent or hallucinate new questions.
- For each exam, include up to 5 representative sample questions, if present.
- If no questions appear for an exam, leave `sample_questions` as an empty list.

Also:
- Group exams by course code.
- If no exam info is found for a particular course, include it with an empty exams list.

Return the result **only** in this structured format:

{format_instructions}

Course codes:
{course_codes}

--- LightRAG CONTEXT (truncated) ---
CONTEXT:
{ctx[:8000]}

REFERENCES:
{refs}

RAW:
{raw}
-------------------------------------
"""

    ai_msg = await llm_instance.ainvoke(prompt)
    try:
        parsed: ExamExtractionResult = exam_parser.parse(ai_msg.content)
    except Exception as e:
        print(f"[exam_fetcher] LLM parse failed, no structured exams: {e}")
        return {}

    exams_by_course: Dict[str, List[Dict[str, Any]]] = {}

    for course in parsed.courses:
        norm_code = course.course_code.replace(" ", "")
        exams_by_course[norm_code] = [
            {
                "name": ex.name,
                "type": ex.type,
                "date": ex.date,
                "coverage": ex.coverage,
                "notes": ex.notes,
                "sample_questions": ex.sample_questions,
            }
            for ex in course.exams
        ]

    return exams_by_course



async def exam_fetcher_node(state: State) -> Dict[str, Any]:


    wants_exams = state.get("wants_exams", False)
    if not wants_exams:
        print("[exam_fetcher] wants_exams=False. Skipping.")
        return {}

    codes = _collect_course_codes(state)
    if not codes:
        print("[exam_fetcher] No course codes available for exam lookup.")
        return {}

    ctx = state.get("lightrag_context", "") or ""
    refs = state.get("lightrag_references", []) or []
    raw = state.get("lightrag_raw", {}) or {}

    print(f"[exam_fetcher] Attempting LLM exam extraction for codes: {codes}")

    exams_by_course = await _extract_exams_with_llm(codes, ctx, refs, raw)

    for code in codes:
        norm_code = code.replace(" ", "")
        exams_by_course.setdefault(norm_code, [])

    print("[exam_fetcher] Exams per course:", {k: len(v) for k, v in exams_by_course.items()})

    return {
        "exams_by_course": exams_by_course
    }
