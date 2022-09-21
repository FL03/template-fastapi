"""
    Appellation: interface
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from fastapi import APIRouter
from app.api.endpoints import users

router = APIRouter(prefix='/api', tags=['v1'])
router.include_router(users.router)


@router.get("/login")
async def login(username: str, password: str):
    return dict(message="Success")


@router.post("/token", tags=['default'])
async def token():
    return dict(token="")
