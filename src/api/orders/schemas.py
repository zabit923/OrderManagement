import uuid
from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Json


class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELED = "canceled"


class ItemSchema(BaseModel):
    title: str
    price: float


class OrderCreate(BaseModel):
    total_price: float
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = datetime.now()

    model_config = ConfigDict(from_attributes=True)


class OrderRead(OrderCreate):
    id: uuid.UUID
    items: Json[Any]
    total_price: float
    status: OrderStatus
    user: "UserRead"

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


from api.users.schemas import UserRead

OrderRead.model_rebuild()
