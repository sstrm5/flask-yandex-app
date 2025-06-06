"""empty message

Revision ID: 390d5e8923ae
Revises: 
Create Date: 2025-05-12 10:54:36.683038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '390d5e8923ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.drop_column('created_date')

    # ### end Alembic commands ###
