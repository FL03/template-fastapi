"""
    Appellation: interface
    Contrib: FL03 <jo3mccain@icloud.com>
    Description:
        ... Summary ...
"""
from fastapi import APIRouter, Depends
from synapse.api.routes import auth, oai, users

from synapse.api.routes.auth import get_current_active_user

router = APIRouter(tags=["v1"])
router.include_router(router=auth.router)
router.include_router(router=oai.router, dependencies=[Depends(get_current_active_user)])
router.include_router(router=users.router)
