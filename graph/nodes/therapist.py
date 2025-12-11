from __future__ import annotations

from graph.state import State
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage

llm_instance = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
)


def therapist_node(state: State) -> dict:
    last_msg = state["messages"][-1]
    user_text = getattr(last_msg, "content", "")

    prompt = f"""
You are a kind, calm, and supportive assistant talking to an engineering student
at the University of Toronto. They might feel stressed, overwhelmed, guilty, or
worried about courses, deadlines, or expectations.

The student wrote:

\"\"\"{user_text}\"\"\"


Your task:
- Gently acknowledge and validate their feelings without judging.
- Normalize that many students struggle with similar things.
- Offer 2–3 practical, small next steps they can take (e.g., break tasks down,
  email a prof/TA, take a short walk, set one tiny goal).
- Encourage them to reach out to real people (friends, family, counsellors)
  if things feel heavy or unsafe.
- Keep the tone warm but not cheesy; avoid toxic positivity.
- Keep the response to about 1–2 short paragraphs plus a short bullet list.
"""

    response = llm_instance.invoke(prompt)
    text = response.content.strip()

    return {
        "messages": [
            AIMessage(content=text)
        ]
    }
