from __future__ import annotations

from graph.state import State
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage

llm_instance = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
)

FALLBACK_PROMPT = """
You are SkuleBot, the UofT Engineering course assistant.

The user asked a question, but:
- The intent router could not classify it confidently, OR
- It does not fit any supported functionality (course lookup, exam lookup, sample questions, etc.)

Your job:
1. Politely acknowledge you may not fully answer the question.
2. Offer a helpful fallback response.
3. Suggest how the user can rephrase their question to match supported tasks
   (course info, exams, sample questions, topics).
4. Keep the tone friendly and concise.

User message:
"{user_message}"
"""


def human_node(state: State) -> dict:
    last_msg = state["messages"][-1]
    user_text = getattr(last_msg, "content", "")

    prompt = FALLBACK_PROMPT.format(user_message=user_text)

    ai_msg = llm_instance.invoke(prompt)
    text = ai_msg.content.strip()

    return {
        "messages": [
            AIMessage(content=text)
        ]
    }
