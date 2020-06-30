"""empty message

Revision ID: 2753aaa378b4
Revises: 
Create Date: 2019-04-14 09:38:11.107169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2753aaa378b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organisations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('address', sa.String(length=240), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=240), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('org_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['org_id'], ['organisations.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entries')
    op.drop_table('organisations')
    # ### end Alembic commands ###
