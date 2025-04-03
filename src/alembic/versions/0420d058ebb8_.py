"""empty message

Revision ID: 0420d058ebb8
Revises: 21bf7d660f1c
Create Date: 2025-04-03 19:56:28.853858

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0420d058ebb8"
down_revision: Union[str, None] = "21bf7d660f1c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.VARCHAR(length=255), nullable=False),
        sa.Column("price", sa.FLOAT(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_items_id"), "items", ["id"], unique=False)
    op.create_table(
        "group_members",
        sa.Column("item_id", sa.Integer(), nullable=False),
        sa.Column("order_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["item_id"],
            ["items.id"],
        ),
        sa.ForeignKeyConstraint(
            ["order_id"],
            ["orders.id"],
        ),
        sa.PrimaryKeyConstraint("item_id", "order_id"),
    )
    op.drop_column("orders", "items")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "orders",
        sa.Column(
            "items",
            postgresql.JSON(astext_type=sa.Text()),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.drop_table("group_members")
    op.drop_index(op.f("ix_items_id"), table_name="items")
    op.drop_table("items")
    # ### end Alembic commands ###
