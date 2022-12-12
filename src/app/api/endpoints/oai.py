"""
    Appellation: auth
    Contrib: FL03 <jo3mccain@icloud.com>
    Description: ... Summary ...
"""
import os
import openai
from fastapi import APIRouter

openai.api_key = os.getenv("OPENAI_SECRET_KEY")

router = APIRouter(prefix="/openai", tags=['openai'])

@router.get("/chat")
async def chat_bot(query: str):
    res = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)

    return {}
