import enum
import uuid
from typing import TYPE_CHECKING, List

from sqlalchemy import FLOAT, JSON, TIMESTAMP, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.models import Base, TableNameMixin

if TYPE_CHECKING:
    from .users import User


class OrderStatus(enum.Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELED = "canceled"


class Order(TableNameMixin, Base):
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    items: Mapped[List[dict]] = mapped_column(JSON, nullable=False)
    total_price: Mapped[float] = mapped_column(FLOAT, nullable=False)
    status: Mapped[OrderStatus] = mapped_column(default=OrderStatus.PENDING)
    created_at: Mapped[func.now()] = mapped_column(
        TIMESTAMP, server_default=func.now(), nullable=False
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="orders",
        lazy="selectin",
        cascade="all, delete",
    )

    def __repr__(self):
        return f"{self.id} - {self.status.value}"
