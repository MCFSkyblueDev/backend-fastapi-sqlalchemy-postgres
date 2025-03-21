"""Add image property

Revision ID: 6db1586b0ed8
Revises: 640424771c67
Create Date: 2025-03-11 01:19:04.930363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6db1586b0ed8'
down_revision: Union[str, None] = '640424771c67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'image')
    # ### end Alembic commands ###
