"""empty message

Revision ID: 0cd29477f736
Revises: 
Create Date: 2020-12-09 20:39:22.886669

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = '0cd29477f736'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estate_agencies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('address', sa.String(length=150), nullable=True),
    sa.Column('complement', sa.String(length=50), nullable=True),
    sa.Column('zip_code', sa.String(length=8), nullable=True),
    sa.Column('number', sa.String(length=10), nullable=True),
    sa.Column('city', sa.String(length=10), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('estates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=7), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('characteristics', sa.JSON(), nullable=False),
    sa.Column('estate_type', sa.String(length=11), nullable=False),
    sa.Column('purpose', sa.String(length=11), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('address', sa.String(length=150), nullable=True),
    sa.Column('complement', sa.String(length=50), nullable=True),
    sa.Column('zip_code', sa.String(length=8), nullable=True),
    sa.Column('number', sa.String(length=10), nullable=True),
    sa.Column('city', sa.String(length=10), nullable=True),
    sa.Column('estate_agency_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['estate_agency_id'], ['estate_agencies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('estates')
    op.drop_table('estate_agencies')
    # ### end Alembic commands ###
