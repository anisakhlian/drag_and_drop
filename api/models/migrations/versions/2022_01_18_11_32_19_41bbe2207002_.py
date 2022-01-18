"""empty message

Revision ID: 41bbe2207002
Revises: b39e7cc61304
Create Date: 2022-01-18 11:32:19.406477

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '41bbe2207002'
down_revision = 'b39e7cc61304'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('documents', sa.Column('order', sa.Integer(), nullable=False))
    op.drop_constraint('documents_parent_id_fkey', 'documents', type_='foreignkey')
    op.drop_column('documents', 'parent_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('documents', sa.Column('parent_id', postgresql.UUID(), autoincrement=False, nullable=True))
    op.create_foreign_key('documents_parent_id_fkey', 'documents', 'documents', ['parent_id'], ['id'], ondelete='CASCADE')
    op.drop_column('documents', 'order')
    # ### end Alembic commands ###
