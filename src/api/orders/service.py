from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_session
from core.database.models import User
from core.database.repositories import OrderRepository

from .schemas import OrderCreate


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    async def create_order(self, order_data: OrderCreate) -> User:
        order_data_dict = order_data.model_dump()
        new_order = User(**order_data_dict)
        await self.repository.create(new_order)
        return new_order


def order_service_factory(
    session: AsyncSession = Depends(get_async_session),
) -> OrderService:
    return OrderService(OrderRepository(session))
