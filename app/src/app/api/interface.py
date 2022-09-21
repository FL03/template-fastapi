"""
    Appellation: interface
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from fastapi import APIRouter
from app.api.endpoints import auth, users

router = APIRouter(tags=['v1'])

router.include_router(router=auth.router)
router.include_router(router=users.router)
