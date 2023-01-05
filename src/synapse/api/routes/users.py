"""
    Appellation: users
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from fastapi import APIRouter, Depends, Form, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from typing import List

from synapse.api.routes.auth import get_current_active_user, auth
from synapse.data.messages import Status
from synapse.data.models import User, UserIn, Users

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[User])
async def get_users():
    return await User.from_queryset(Users.all())


@router.post("/user", response_model=User)
async def create_user(username: str = Form(), password: str = Form()):
    hashed_password = auth.hash_password(password)
    user_obj = await Users.create(**dict(username=username, hashed_password=hashed_password))
    return await User.from_tortoise_orm(user_obj)


@router.get(
    "/user/{uid}",
    response_model=User,
    responses={404: dict(model=HTTPNotFoundError)},
)
async def get_user(uid: int):
    return await User.from_queryset_single(Users.get(id=uid))


@router.put(
    "/user/{user_id}",
    response_model=User,
    responses={404: dict(model=HTTPNotFoundError)},
)
async def update_user(user_id: int, usr: User = Depends(get_current_active_user)):
    await Users.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await User.from_queryset_single(Users.get(id=user_id))


@router.delete(
    "/user/{user_id}",
    response_model=Status,
    responses={404: dict(model=HTTPNotFoundError)},
)
async def delete_user(user_id, usr: User = Depends(get_current_active_user)):
    deleted_count = await Users.filter(id=usr.id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")
