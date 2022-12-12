"""
    Appellation: interface
    Contrib: FL03 <jo3mccain@icloud.com>
    Description:
        ... Summary ...
"""
from fastapi import APIRouter
from app.api.endpoints import auth, fido, oai, users

router = APIRouter(tags=['v1'])

router.include_router(router=auth.router)
router.include_router(router=fido.router)
router.include_router(router=oai.router)
router.include_router(router=users.router)
