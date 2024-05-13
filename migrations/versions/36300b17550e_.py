"""empty message

Revision ID: 36300b17550e
Revises: 
Create Date: 2024-05-13 11:14:59.640911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36300b17550e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reptiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reptiles')
    # ### end Alembic commands ###
