"""create quiz table

Revision ID: 1e2531a281b4
Revises:
Create Date: 2025-05-06 16:40:39.328065

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1e2531a281b4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "quiz",
        sa.Column("id", sa.Uuid, primary_key=True),
        sa.Column("title", sa.String(255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("quiz")
