"""empty message

Revision ID: 7ea1bb3fef6c
Revises: 9527f3560944
Create Date: 2024-07-20 08:03:11.492645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ea1bb3fef6c'
down_revision = '9527f3560944'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('birthday',
               existing_type=sa.DATE(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('birthday',
               existing_type=sa.DATE(),
               nullable=False)

    # ### end Alembic commands ###
