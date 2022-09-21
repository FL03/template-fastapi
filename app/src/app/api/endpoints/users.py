"""
    Appellation: users
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from fastapi import APIRouter

router = APIRouter(prefix='/users', tags=['users'])


@router.get("/")
async def public_user_feed():
    return dict(message='Success')
