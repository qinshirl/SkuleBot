
from fastapi import FastAPI
from pydantic import BaseModel

from service import skulebot_chat

app = FastAPI(title="SkuleBot API")


class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str


@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest) -> ChatResponse:
    reply = await skulebot_chat(req.message)
    return ChatResponse(reply=reply)
