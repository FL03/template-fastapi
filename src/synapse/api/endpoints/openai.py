"""
    Appellation: openai
    Contrib: FL03 <jo3mccain@icloud.com>
    Description: ... Summary ...
"""
from fastapi import APIRouter, HTTPException
from typing import List, Dict

from synapse.data.messages import Status

router = APIRouter(prefix="/openai", tags=["openai"])


@router.get("/", response_model=Dict)
async def landing():
    return dict(message="OpenAI Router")
