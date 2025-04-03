from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from .schemas import Token, UserCreate, UserRead
from .service import UserService, user_service_factory

router = APIRouter(prefix="")


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def register_user(
    user_data: UserCreate,
    user_service: UserService = Depends(user_service_factory),
):
    new_user = await user_service.create_user(user_data)
    return new_user


@router.post("/token", status_code=status.HTTP_201_CREATED, response_model=Token)
async def login_user(
    login_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    user_service: UserService = Depends(user_service_factory),
):
    tokens = await user_service.authenticate_user(login_data)
    return {
        "access_token": tokens["access_token"],
        "refresh_token": tokens["refresh_token"],
    }
