"""empty message

Revision ID: a09a085b8d02
Revises: 8cf092c26109
Create Date: 2020-07-01 09:58:01.371038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a09a085b8d02'
down_revision = '8cf092c26109'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('herolo_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_herolo_users_name'), 'herolo_users', ['name'], unique=False)
    op.create_table('herolo_messages',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('reciever_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=300), nullable=True),
    sa.Column('subject', sa.String(length=300), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['reciever_id'], ['herolo_users.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['sender_id'], ['herolo_users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('message_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('herolo_messages')
    op.drop_index(op.f('ix_herolo_users_name'), table_name='herolo_users')
    op.drop_table('herolo_users')
    # ### end Alembic commands ###
