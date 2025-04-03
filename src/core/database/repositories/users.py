from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.database.models import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> Sequence[User]:
        statement = select(User)
        result = await self.session.execute(statement)
        users = result.scalars().all()
        return users

    async def get_by_id(self, user_id: int) -> User:
        statement = select(User).where(User.id == user_id)
        result = await self.session.execute(statement)
        return result.scalars().first()

    async def get_by_email(self, email: str) -> User:
        statement = select(User).where(User.email == email)
        result = await self.session.execute(statement)
        return result.scalars().first()

    async def create(self, user: User) -> None:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
