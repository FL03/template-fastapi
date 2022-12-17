"""
    Appellation: interface
    Contrib: FL03 <jo3mccain@icloud.com>
    Description:
        ... Summary ...
"""
from fastapi import APIRouter
from synapse.api.endpoints import  users

router = APIRouter(tags=['v1'])

router.include_router(router=users.router)
