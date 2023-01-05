"""
    Appellation: interface
    Contrib: FL03 <jo3mccain@icloud.com>
    Description:
        ... Summary ...
"""
from fastapi import APIRouter
from synapse.api.routes import auth, oai, payments, users

router = APIRouter(tags=["v1"])
router.include_router(router=auth.router)
router.include_router(router=oai.router)
router.include_router(router=payments.router)
router.include_router(router=users.router)
