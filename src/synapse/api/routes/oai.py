"""
    Appellation: openai
    Contrib: FL03 <jo3mccain@icloud.com>
    Description: ... Summary ...
"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict

from synapse.api.routes.auth import get_current_active_user
from synapse.data.messages import Status
from synapse.data.models.users import User
import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")
router = APIRouter(prefix="/openai", tags=["openai"])


@router.get("/", response_model=Dict)
async def landing(current_user: User = Depends(get_current_active_user)):
    return dict(message="OpenAI Router")


@router.get("/chatgpt/{prompt}")
async def chatgpt3_completion(prompt: str, temp: float = 0.5, max_tokens: int = 2000, current_user: User = Depends(get_current_active_user)):
    completion = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, temperature=temp, max_tokens=max_tokens
    )
    return [dict(i) for i in completion.choices.text]


@router.get("/codex/{prompt}")
async def codex_completion(prompt: str, temp: float = 0.5, max_tokens: int = 2000, current_user: User = Depends(get_current_active_user)):
    completion = openai.Completion.create(
        model="text-davinci-002", prompt=prompt, temperature=temp, max_tokens=max_tokens
    )
    return [dict(i) for i in completion.choices]
