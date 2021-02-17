"""users files table

Revision ID: 475dbf7b99b6
Revises: 14ec4b83d0c1
Create Date: 2021-01-31 22:45:21.540278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '475dbf7b99b6'
down_revision = '14ec4b83d0c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_files')
    # ### end Alembic commands ###
