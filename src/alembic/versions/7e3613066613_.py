"""empty message

Revision ID: 7e3613066613
Revises: 059a05b0bb59
Create Date: 2025-04-02 15:47:11.386360

"""
from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "7e3613066613"
down_revision: Union[str, None] = "059a05b0bb59"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
