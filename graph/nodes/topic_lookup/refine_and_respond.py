from __future__ import annotations

from typing import Dict, Any
from langchain.chat_models import init_chat_model

from graph.state import State

llm = init_chat_model("openai:gpt-4.1")


async def refine_and_respond_node(state: State) -> Dict[str, Any]:

    user_query = state["messages"][-1].content

    selected_course = state.get("selected_course")
    course_info = state.get("course_info")
    exam_content = state.get("exam_content")
    suggested_courses = state.get("suggested_courses") or []

    rag_context = state.get("lightrag_context", "")
    rag_refs = state.get("lightrag_references", [])
    rag_raw = state.get("lightrag_raw", {})

    wants_exams = state.get("wants_exams", False)


    prompt = f"""
You are SkuleBot, an academic assistant for University of Toronto Engineering students.

USER QUESTION:
{user_query}


PIPELINE RESULTS:
Selected Course:
{selected_course}

Course Info:
{course_info}

Suggested Courses (if multiple):
{suggested_courses}

Exam Content (if any):
{exam_content}

LightRAG Context:
{rag_context}

LightRAG References:
{rag_refs}

Raw RAG Output:
{rag_raw}
----------------------------------------

INSTRUCTIONS FOR YOUR RESPONSE:
1. Fully answer the student's question.
2. Use **course_info** if available.
3. If multiple courses were suggested, compare them cleanly.
4. If exams exist and user wants them, include structured exam help.
5. Use LightRAG context only for enrichment (no raw dumps).
6. Keep the final answer concise and accurate.
7. If the retrieved data is irrelevant/noisy, ignore it.
8. If nothing useful exists, say so politely and still give helpful guidance.

Your final output must be a single clear answer.
if the there is no exact content and you are making up questions - indicate that clearly to students at the end
    """


    print("[refine_and_respond] Calling LLM for final polish...")
    response = await llm.ainvoke(prompt)
    final_answer = response.content.strip()

    return {
        "messages": [
            {
                "role": "assistant",
                "content": final_answer
            }
        ]
    }
