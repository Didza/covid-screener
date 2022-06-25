"""init_migration

Revision ID: 42fca4f92c76
Revises: 
Create Date: 2022-06-24 22:02:00.263782+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from covid_screener.adapters.orm import GUID

revision = '42fca4f92c76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('uuid', GUID(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_departments_is_active'), 'departments', ['is_active'], unique=False)
    op.create_index(op.f('ix_departments_name'), 'departments', ['name'], unique=True)
    op.create_table('symptoms',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('uuid', GUID(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('has_fever', sa.Boolean(), nullable=False),
    sa.Column('has_cough', sa.Boolean(), nullable=False),
    sa.Column('has_shortness_of_breath', sa.Boolean(), nullable=False),
    sa.Column('has_fatigue', sa.Boolean(), nullable=False),
    sa.Column('has_body_aches', sa.Boolean(), nullable=False),
    sa.Column('has_loss_of_taste', sa.Boolean(), nullable=False),
    sa.Column('has_loss_of_smell', sa.Boolean(), nullable=False),
    sa.Column('has_sore_throat', sa.Boolean(), nullable=False),
    sa.Column('has_runny_nose', sa.Boolean(), nullable=False),
    sa.Column('has_nausea', sa.Boolean(), nullable=False),
    sa.Column('is_vomiting', sa.Boolean(), nullable=False),
    sa.Column('has_diarrhea', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_symptoms_is_active'), 'symptoms', ['is_active'], unique=False)
    op.create_table('employees',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('uuid', GUID(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('surname', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_employees_department_id'), 'employees', ['department_id'], unique=False)
    op.create_index(op.f('ix_employees_email'), 'employees', ['email'], unique=True)
    op.create_index(op.f('ix_employees_is_active'), 'employees', ['is_active'], unique=False)
    op.create_index(op.f('ix_employees_username'), 'employees', ['username'], unique=True)
    op.create_table('questionnaires',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('uuid', GUID(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('has_tested_positive', sa.Boolean(), nullable=False),
    sa.Column('awaiting_test_results', sa.Boolean(), nullable=False),
    sa.Column('positive_in_last_fortnight', sa.Boolean(), nullable=False),
    sa.Column('is_vaccinated', sa.Boolean(), nullable=False),
    sa.Column('symptom_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['symptom_id'], ['symptoms.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_questionnaires_is_active'), 'questionnaires', ['is_active'], unique=False)
    op.create_table('screenings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('uuid', GUID(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('questionnaire_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['questionnaire_id'], ['questionnaires.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_screenings_is_active'), 'screenings', ['is_active'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_screenings_is_active'), table_name='screenings')
    op.drop_table('screenings')
    op.drop_index(op.f('ix_questionnaires_is_active'), table_name='questionnaires')
    op.drop_table('questionnaires')
    op.drop_index(op.f('ix_employees_username'), table_name='employees')
    op.drop_index(op.f('ix_employees_is_active'), table_name='employees')
    op.drop_index(op.f('ix_employees_email'), table_name='employees')
    op.drop_index(op.f('ix_employees_department_id'), table_name='employees')
    op.drop_table('employees')
    op.drop_index(op.f('ix_symptoms_is_active'), table_name='symptoms')
    op.drop_table('symptoms')
    op.drop_index(op.f('ix_departments_name'), table_name='departments')
    op.drop_index(op.f('ix_departments_is_active'), table_name='departments')
    op.drop_table('departments')
    # ### end Alembic commands ###
