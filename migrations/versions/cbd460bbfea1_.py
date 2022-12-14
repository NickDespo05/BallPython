"""empty message

Revision ID: cbd460bbfea1
Revises: 
Create Date: 2022-10-25 19:27:05.624383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbd460bbfea1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reptiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('common_name', sa.String(length=250), nullable=True),
    sa.Column('scientific_name', sa.String(length=250), nullable=True),
    sa.Column('conservation_status', sa.String(length=250), nullable=True),
    sa.Column('native_habitat', sa.String(length=250), nullable=True),
    sa.Column('fun_fact', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reptiles')
    # ### end Alembic commands ###
