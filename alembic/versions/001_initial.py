"""Initial migration

Revision ID: 001_initial
Revises: 
Create Date: 2026-04-18 13:20:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'api_logs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('endpoint', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_api_logs_id'), 'api_logs', ['id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_api_logs_id'), table_name='api_logs')
    op.drop_table('api_logs')
