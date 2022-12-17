"""
    Appellation: interface
    Contrib: FL03 <jo3mccain@icloud.com>
    Description:
        ... Summary ...
"""
from fastapi import APIRouter
from synapse.api.endpoints import openai, users

router = APIRouter(tags=["v1"])
router.include_router(router=openai.router)
router.include_router(router=users.router)
