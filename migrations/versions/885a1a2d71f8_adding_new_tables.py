"""Adding new tables

Revision ID: 885a1a2d71f8
Revises: baeedf9a66ed
Create Date: 2025-03-07 20:34:20.336983

"""
import sqlmodel
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '885a1a2d71f8'
down_revision: Union[str, None] = 'baeedf9a66ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manager',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('bio', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('phone_number', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('office_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['office_id'], ['office.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owner',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('bio', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('phone_number', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('office_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['office_id'], ['office.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('office_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['office_id'], ['office.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory',
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('product_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('office_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['office_id'], ['office.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patientexam',
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('date_time', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('status', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('patient_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('doctor_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patienthistory',
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('date_time', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('patient_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('doctor_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('doctor', sa.Column('bio', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('doctor', sa.Column('phone_number', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('doctor', sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('doctor', sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.drop_column('doctor', 'description')
    op.add_column('patient', sa.Column('bio', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('patient', sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('patient', sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('user', sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'username')
    op.drop_column('patient', 'address')
    op.drop_column('patient', 'email')
    op.drop_column('patient', 'bio')
    op.add_column('doctor', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('doctor', 'address')
    op.drop_column('doctor', 'email')
    op.drop_column('doctor', 'phone_number')
    op.drop_column('doctor', 'bio')
    op.drop_table('patienthistory')
    op.drop_table('patientexam')
    op.drop_table('inventory')
    op.drop_table('product')
    op.drop_table('owner')
    op.drop_table('manager')
    # ### end Alembic commands ###
