import asyncio

from api.users.utils import bcrypt_context
from core.database.db import async_session_maker
from core.database.models import User


async def create_superuser():
    async with async_session_maker() as session:
        email = input("Enter email: ")
        password = input("Enter password: ")

        hashed_password = bcrypt_context.hash(password)

        superuser = User(
            email=email,
            password=hashed_password,
            is_superuser=True,
        )

        session.add(superuser)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(create_superuser())
