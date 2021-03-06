"""Nova coluna Tamanhos

Revision ID: b1821ecf0544
Revises: 46a0c6c9206a
Create Date: 2021-11-05 14:35:43.568272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1821ecf0544'
down_revision = '46a0c6c9206a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('tamanhos', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('produto', 'tamanhos')
    # ### end Alembic commands ###
