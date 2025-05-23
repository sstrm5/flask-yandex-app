"""empty message

Revision ID: 3aeff8707604
Revises: 390d5e8923ae
Create Date: 2025-05-12 10:55:37.937809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aeff8707604'
down_revision = '390d5e8923ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_date', sa.DATETIME(), nullable=True))
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
