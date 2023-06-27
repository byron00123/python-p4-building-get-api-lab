"""Add name column to bakeries table

Revision ID: 122f6203fe02
Revises: a50cde241c4b
Create Date: 2023-06-27 11:27:53.870034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '122f6203fe02'
down_revision = 'a50cde241c4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('bakery_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=True))
        batch_op.create_foreign_key('fk_baked_goods_bakery_id', 'bakeries', ['bakery_id'], ['id'])

    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.drop_column('name')

    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.drop_constraint('fk_baked_goods_bakery_id', type_='foreignkey')
        batch_op.drop_column('price')
        batch_op.drop_column('bakery_id')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
