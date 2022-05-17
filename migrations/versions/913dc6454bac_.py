"""empty message

Revision ID: 913dc6454bac
Revises: bbfcf14710b0
Create Date: 2022-05-17 22:36:36.539635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '913dc6454bac'
down_revision = 'bbfcf14710b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('homeplanet_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'people', 'planet', ['homeplanet_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'people', type_='foreignkey')
    op.drop_column('people', 'homeplanet_id')
    # ### end Alembic commands ###