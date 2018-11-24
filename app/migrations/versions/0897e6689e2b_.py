"""empty message

Revision ID: 0897e6689e2b
Revises: 513e2113dd08
Create Date: 2018-11-24 08:09:44.791197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0897e6689e2b'
down_revision = '513e2113dd08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('session_token', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'session_token')
    # ### end Alembic commands ###
