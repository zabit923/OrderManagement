from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core.database import get_async_session
from core.database.models import User
from core.database.repositories import UserRepository

from .schemas import UserCreate
from .utils import create_token, generate_passwd_hash, verify_password


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_user_by_id(self, user_id: int) -> User:
        user = await self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        return user

    async def get_user_by_email(self, email: str) -> User:
        user = await self.repository.get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        return user

    async def create_user(self, user_data: UserCreate) -> User:
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        new_user.password = generate_passwd_hash(user_data_dict["password"])
        await self.repository.create(new_user)
        return new_user

    async def authenticate_user(
        self, login_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ):
        user = await self.get_user_by_email(login_data.username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate user.",
            )
        password_valid = verify_password(
            password=login_data.password, password_hash=user.password
        )
        if password_valid:
            access_token = create_token(
                email=user.email,
                user_id=user.id,
                expires_delta=timedelta(hours=24),
            )
            refresh_token = create_token(
                email=user.email,
                user_id=user.id,
                expires_delta=timedelta(days=2),
                refresh=True,
            )
            return {"access_token": access_token, "refresh_token": refresh_token}
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials."
        )


def user_service_factory(
    session: AsyncSession = Depends(get_async_session),
) -> UserService:
    return UserService(UserRepository(session))
