"""empty message

Revision ID: 83b0e8b8a654
Revises: f8edd5739607
Create Date: 2020-07-01 03:12:04.043211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83b0e8b8a654'
down_revision = 'f8edd5739607'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'herolo_messages', 'herolo_users', ['sender_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'herolo_messages', 'herolo_users', ['reciever_id'], ['id'], ondelete='SET NULL')
    op.drop_column('herolo_messages', 'first_name')
    op.drop_column('herolo_messages', 'chat_id')
    op.drop_column('herolo_messages', 'username')
    op.drop_column('herolo_messages', 'chat_title')
    op.drop_column('herolo_messages', 'user_id')
    op.drop_column('herolo_messages', 'text')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('herolo_messages', sa.Column('text', sa.VARCHAR(length=300), nullable=True))
    op.add_column('herolo_messages', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.add_column('herolo_messages', sa.Column('chat_title', sa.VARCHAR(length=240), nullable=True))
    op.add_column('herolo_messages', sa.Column('username', sa.VARCHAR(length=240), nullable=True))
    op.add_column('herolo_messages', sa.Column('chat_id', sa.INTEGER(), nullable=True))
    op.add_column('herolo_messages', sa.Column('first_name', sa.VARCHAR(length=240), nullable=True))
    op.drop_constraint(None, 'herolo_messages', type_='foreignkey')
    op.drop_constraint(None, 'herolo_messages', type_='foreignkey')
    # ### end Alembic commands ###
