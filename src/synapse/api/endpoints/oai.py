"""
    Appellation: openai
    Contrib: FL03 <jo3mccain@icloud.com>
    Description: ... Summary ...
"""
from fastapi import APIRouter, HTTPException
from typing import List, Dict

from synapse.data.messages import Status
import openai, os

openai.api_key = os.getenv("OPENAI_SECRET_KEY")
router = APIRouter(prefix="/openai", tags=["openai"])


@router.get("/", response_model=Dict)
async def landing():
    return dict(message="OpenAI Router")


@router.get("/chatgpt/{prompt}")
async def chatgpt3_completion(prompt: str, temp: int = 0, max_tokens: int = 7):
    completion = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, temperature=temp, max_tokens=max_tokens
    )
    return [dict(i) for i in completion.choices]


@router.get("/codex/{prompt}")
async def codex_completion(prompt: str, temp: int = 0, max_tokens: int = 8000):
    completion = openai.Completion.create(
        model="text-davinci-002", prompt=prompt, temperature=temp, max_tokens=max_tokens
    )
    return [dict(i) for i in completion.choices]
