from sqlalchemy.ext.asyncio import AsyncSession

from core.database.models import Order


class OrderRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, order: Order) -> None:
        self.session.add(order)
        await self.session.commit()
        await self.session.refresh(order)
