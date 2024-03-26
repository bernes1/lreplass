"""initial migration

Revision ID: d5015d723924
Revises: 
Create Date: 2024-03-07 23:22:48.154265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5015d723924'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("username", sa.String, unique=True),
        sa.Column("hashed_password", sa.String)
    )
    op.create_table(
        "job_listings",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("company_name", sa.String),
        sa.Column("position", sa.String),
        sa.Column("location", sa.String),
        sa.Column("application_deadline", sa.Date),
        sa.Column("date_posted", sa.Date),
        sa.Column("number_of_positions", sa.Integer),
        sa.Column("job_ad_link", sa.String)
    )


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("job_listings")

