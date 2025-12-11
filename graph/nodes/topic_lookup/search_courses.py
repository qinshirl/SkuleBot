#
#
# from __future__ import annotations
#
# import re
# from typing import Dict, Any, List
#
# from graph.state import State
# from graph.nodes.topic_lookup.lightrag_core import lightrag_retrieve
#
#
# def _extract_course_codes_from_references(refs: List[Dict[str, Any]]) -> List[str]:
#
#     results = []
#
#     pattern = re.compile(r"\b([A-Z]{3}\s?\d{3}[A-Z]?)\b")
#
#     for ref in refs:
#         file_path = ref.get("file_path", "") or ""
#         ref_id = ref.get("reference_id", "") or ""
#
#         for text in (file_path, ref_id):
#             matches = pattern.findall(text)
#             for m in matches:
#                 results.append(m.replace(" ", ""))  # normalize ECE 231 -> ECE231
#
#     return list(set(results))
#
#
# async def search_courses_node(state: State) -> Dict[str, Any]:
#     print("[search_courses] Starting LightRAG retrieval search")
#
#     course_query = state.get("course_query")
#     last_msg = state["messages"][-1]
#     last_user_message = getattr(last_msg, "content", "")
#
#     query_text = (course_query or last_user_message or "").strip()
#
#     if not query_text:
#         print("[search_courses] No query text found.")
#         return {
#             "suggested_courses": [],
#             "messages": [{
#                 "role": "assistant",
#                 "content": "I couldn't find a course or topic in your request."
#             }]
#         }
#
#     retrieval = await lightrag_retrieve(query_text)
#     kg_result = retrieval.get("references", [])
#
#
#     extracted_codes = _extract_course_codes_from_references(kg_result)
#     # ctx = retrieval.get("context", "")
#
#     # print(f"[search_courses] RAG returned {len(refs)} reference objects")
#     # print("[search_courses] Context snippet:", repr(ctx[:200]))
#     print(f"[search_courses] Extracted course codes: {extracted_codes}")
#
#     updates: Dict[str, Any] = {}
#
#     updates["lightrag_context"] = kg_result
#
#
#     if not extracted_codes:
#         updates["suggested_courses"] = []
#         print("[search_courses] No course codes found.")
#         return updates
#
#     if len(extracted_codes) == 1:
#         course_code = extracted_codes[0]
#         print(f"[search_courses] One match: {course_code}")
#
#         updates["selected_course"] = {
#             "code": course_code,
#             "source": "LightRAG",
#             "description": "Matched via LightRAG references."
#         }
#         return updates
#
#     print("[search_courses] Multiple course matches found.")
#     updates["suggested_courses"] = [
#         {"code": c, "source": "LightRAG", "description": "Possible match"}
#         for c in extracted_codes
#     ]
#
#     return updates





# from __future__ import annotations
#
# import re
# from typing import Dict, Any, List
#
# from langchain.chat_models import init_chat_model
# from langchain_core.output_parsers import PydanticOutputParser
# from pydantic import BaseModel, Field
#
# from graph.state import State
# from graph.nodes.topic_lookup.lightrag_core import lightrag_retrieve
#
# llm = init_chat_model("openai:gpt-4.1")
#
# class CourseCodeList(BaseModel):
#     course_codes: List[str] = Field(
#         default_factory=list,
#         description="List of normalized UofT course codes like MAT186H1F, MAT187, ECE1724H1"
#     )
#
# parser = PydanticOutputParser(pydantic_object=CourseCodeList)
#
# COURSE_CODE_REGEX = re.compile(r"\b([A-Z]{3}\s?\d{3}[A-Z]?)\b")
#
# def _regex_candidates_from_text(text: str) -> List[str]:
#
#     if not text:
#         return []
#     candidates = {m.replace(" ", "") for m in COURSE_CODE_REGEX.findall(text)}
#     return sorted(candidates)
#
# async def _extract_course_codes_with_llm(raw_text: str) -> List[str]:
#     if not raw_text:
#         return []
#
#     candidates = _regex_candidates_from_text(raw_text)
#     if not candidates:
#         return []
#
#     format_instructions = parser.get_format_instructions()
#
#     prompt = f"""
# You are extracting **University of Toronto course codes** from noisy text.
#
# Examples of valid course codes (pattern only, they may or may not appear):
# - MAT186H1F
# - MAT187
# - ECE1724H1
# - CSC207H1S
# - APS1080H
#
# You are given:
# 1. A list of candidate strings that might be course codes.
# 2. A chunk of text (LightRAG output) where they came from.
#
# Your job:
# - Keep only the items that clearly correspond to actual course identifiers.
# - Normalize them by removing internal spaces, e.g. "MAT 187" -> "MAT187".
# - Remove duplicates.
# - **Ignore** section numbers ("Lec0101"), dates, quiz/assignment names,
#   page/section numbers (e.g., "Sec 2.4"), durations, etc.
#
# Return the result using this format:
#
# {format_instructions}
#
# Candidate strings:
# {candidates}
#
# Context text (truncated):
# ```text
# {raw_text[:8000]}
# ```"""
#
#     ai_msg = await llm.ainvoke(prompt)
#
#     try:
#         parsed: CourseCodeList = parser.parse(ai_msg.content)
#         cleaned = sorted({c.replace(" ", "") for c in parsed.course_codes if c})
#         if cleaned:
#             return cleaned
#     except Exception as e:
#
#         print(f"[search_courses] LLM parse error, falling back to regex candidates: {e}")
#
#     return candidates
#
# async def search_courses_node(state: State) -> Dict[str, Any]:
#     print("[search_courses] Starting LightRAG retrieval search")
#
#     course_query = state.get("course_query")
#     last_msg = state["messages"][-1]
#     last_user_message = getattr(last_msg, "content", "")
#
#     query_text = (course_query or last_user_message or "").strip()
#
#     if not query_text:
#         print("[search_courses] No query text found.")
#         return {
#             "suggested_courses": [],
#             "messages": [{
#                 "role": "assistant",
#                 "content": "I couldn't find a course or topic in your request."
#             }]
#         }
#
#     retrieval = await lightrag_retrieve(query_text)
#
#     raw_text = retrieval.get("raw", "") or ""
#     print(f"[search_courses] Length of LightRAG raw text: {len(raw_text)}")
#
#     updates: Dict[str, Any] = {}
#
#     updates["lightrag_context"] = raw_text
#
#     extracted_codes = await _extract_course_codes_with_llm(raw_text)
#     print(f"[search_courses] Extracted course codes (LLM): {extracted_codes}")
#
#     if not extracted_codes:
#         updates["suggested_courses"] = []
#         print("[search_courses] No course codes found.")
#         return updates
#
#     if len(extracted_codes) == 1:
#         course_code = extracted_codes[0]
#         print(f"[search_courses] One match: {course_code}")
#
#         updates["selected_course"] = {
#             "code": course_code,
#             "source": "LightRAG+LLM",
#             "description": "Matched via LightRAG raw output and LLM extraction.",
#         }
#         return updates
#
#     print("[search_courses] Multiple course matches found.")
#     updates["suggested_courses"] = [
#         {
#             "code": c,
#             "source": "LightRAG+LLM",
#             "description": "Possible match from LightRAG output",
#         }
#         for c in extracted_codes
#     ]
#
#     return updates
#

from __future__ import annotations

import re
from typing import Dict, Any, List

from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from graph.state import State
from graph.nodes.topic_lookup.lightrag_core import lightrag_retrieve

llm = init_chat_model("openai:gpt-4.1")


class CourseCodeList(BaseModel):
    course_codes: List[str] = Field(
        default_factory=list,
        description="List of normalized UofT course codes like MAT186H1F, MAT187, ECE1724H1"
    )


parser = PydanticOutputParser(pydantic_object=CourseCodeList)

COURSE_CODE_REGEX = re.compile(r"\b([A-Z]{3}\s?\d{3}[A-Z]?)\b")


def _regex_candidates_from_text(text: str) -> List[str]:
    if not text:
        return []
    candidates = {m.replace(" ", "") for m in COURSE_CODE_REGEX.findall(text)}
    return sorted(candidates)


async def _extract_course_codes_with_llm(raw_text: str) -> List[str]:
    if not raw_text:
        return []

    candidates = _regex_candidates_from_text(raw_text)
    if not candidates:
        return []

    format_instructions = parser.get_format_instructions()

    prompt = f"""
You are extracting **University of Toronto course codes** from text.

Valid patterns resemble:
- MAT186H1F
- MAT187
- ECE1724H1
- CSC207H1S
- APS1080H

You are given:
1. A list of candidate strings from regex.
2. A chunk of text (RAG output).

Your job:
- Keep only real course identifiers.
- Normalize them by removing spaces, e.g., "MAT 187" -> "MAT187".
- Ignore section numbers, dates, quiz names, page/section numbers, durations, etc.

Return using this JSON structure:
{format_instructions}

Candidates:
{candidates}

Text:
```text
{raw_text[:8000]}
```
"""

    ai_msg = await llm.ainvoke(prompt)

    try:
        parsed: CourseCodeList = parser.parse(ai_msg.content)
        cleaned = sorted({c.replace(" ", "") for c in parsed.course_codes if c})
        if cleaned:
            return cleaned
    except Exception as e:
        print(f"[search_courses] LLM parse error, falling back to regex candidates: {e}")

    return candidates

async def _is_followup_for_course(user_message: str, course_code: str) -> bool:
    if not course_code:
        return False

    prompt = f"""
You are helping a course assistant keep track of which course the user is talking about.

Previously, we resolved the course to: "{course_code}".

Now the user says:
"{user_message}"

Question:
Is the user clearly talking about this same course (even if they use words like "it", "this course", "that class", etc.)?

Answer with a single word: YES or NO.
"""

    resp = await llm.ainvoke(prompt)
    answer = resp.content.strip().upper()
    return answer.startswith("YES")

async def search_courses_node(state: State) -> Dict[str, Any]:
    print("[search_courses] Starting LightRAG retrieval search")

    last_msg = state["messages"][-1]
    last_user_message = getattr(last_msg, "content", "")

    course_query = state.get("course_query")
    query_text = (course_query or last_user_message or "").strip()

    current_course_code = state.get("current_course_code")
    previous_context = state.get("lightrag_context") or ""
    last_course_query = state.get("last_course_query")

    if current_course_code:
        print(f"[search_courses] Current course in memory: {current_course_code}")
        is_followup = await _is_followup_for_course(
            user_message=last_user_message,
            course_code=current_course_code,
        )
        if is_followup and previous_context:
            print("[search_courses] LLM says this is a follow-up; reusing previous context.")
            return {
                "selected_course": {
                    "code": current_course_code,
                    "source": "conversation_memory",
                },
                "lightrag_context": previous_context,
            }
        else:
            print("[search_courses] Not treated as follow-up; doing a fresh search.")

    # if empty query
    if not query_text:
        print("[search_courses] No query text found.")
        return {
            "suggested_courses": [],
            "messages": [{
                "role": "assistant",
                "content": "I couldn't find a course or topic in your request."
            }]
        }
    # lightrag
    retrieval = await lightrag_retrieve(query_text)

    raw_text = retrieval.get("raw", "") or ""
    print(f"[search_courses] Length of LightRAG raw text: {len(raw_text)}")

    updates: Dict[str, Any] = {}

    # Store the context we just got
    updates["lightrag_context"] = raw_text
    updates["last_course_query"] = query_text

    extracted_codes = await _extract_course_codes_with_llm(raw_text)
    print(f"[search_courses] Extracted course codes (LLM): {extracted_codes}")

    if not extracted_codes:
        updates["suggested_courses"] = []
        print("[search_courses] No course codes found.")
        return updates

    explicit_from_query = _regex_candidates_from_text(query_text)
    chosen_code = None

    if len(extracted_codes) > 1 and len(explicit_from_query) == 1:
        user_code = explicit_from_query[0]
        print(f"[search_courses] User explicitly mentioned: {user_code}")

        narrowed = [
            c for c in extracted_codes
            if c.startswith(user_code) or user_code in c
        ]

        print(f"[search_courses] Narrowed candidates based on user input: {narrowed}")

        if len(narrowed) == 1:
            chosen_code = narrowed[0]

    if chosen_code is None and len(extracted_codes) == 1:
        chosen_code = extracted_codes[0]

    if chosen_code is not None:
        print(f"[search_courses] Resolved single course: {chosen_code}")

        updates["selected_course"] = {
            "code": chosen_code,
            "source": "LightRAG+LLM",
            "description": "Matched via LightRAG raw output and LLM extraction (with user hint).",
        }

        updates["current_course_code"] = chosen_code

        return updates

    print("[search_courses] Multiple course matches remain; suggesting options.")
    updates["suggested_courses"] = [
        {
            "code": c,
            "source": "LightRAG+LLM",
            "description": "Possible match from LightRAG output",
        }
        for c in extracted_codes
    ]

    return updates
