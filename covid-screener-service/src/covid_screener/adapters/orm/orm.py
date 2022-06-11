from sqlalchemy import (
    Table, MetaData, Column, Integer, String, ForeignKey,
    Boolean
)
from sqlalchemy.orm import mapper, relationship

from covid_screener.domain.model.screening import Department, Employee, \
    Symptom, Questionnaire, Screening


from . import get_standard_columns

metadata = MetaData()

departments = Table(
    'departments', metadata,
    *get_standard_columns(),
    Column('name', String(100), nullable=False, index=True)
)

employees = Table(
    'employees', metadata,
    *get_standard_columns(),
    Column('username', String(100), nullable=False, index=True),
    Column('name', String(100), nullable=False),
    Column('surname', String(100), nullable=False),
    Column('email', String(100), nullable=False, index=True),
    Column('is_admin', Boolean, nullable=False),
    Column('department_id', Integer, ForeignKey('departments.id'), index=True),
)

symptoms = Table(
    'symptoms', metadata,
    *get_standard_columns(),
    Column('has_fever', Boolean, nullable=False),
    Column('has_cough', Boolean, nullable=False),
    Column('has_shortness_of_breath', Boolean, nullable=False),
    Column('has_fatigue', Boolean, nullable=False),
    Column('has_body_aches', Boolean, nullable=False),
    Column('has_loss_of_taste', Boolean, nullable=False),
    Column('has_loss_of_smell', Boolean, nullable=False),
    Column('has_sore_throat', Boolean, nullable=False),
    Column('has_runny_nose', Boolean, nullable=False),
    Column('has_nausea', Boolean, nullable=False),
    Column('is_vomiting', Boolean, nullable=False),
    Column('has_diarrhea', Boolean, nullable=False),
)

questionnaires = Table(
    'questionnaires', metadata,
    *get_standard_columns(),
    Column('has_tested_positive', Boolean, nullable=False),
    Column('awaiting_test_results', Boolean, nullable=False),
    Column('positive_in_last_fortnight', Boolean, nullable=False),
    Column('is_vaccinated', Boolean, nullable=False),
    Column('symptom_id', Integer, ForeignKey('symptoms.id'), nullable=False),
)

screenings = Table(
    'screenings', metadata,
    *get_standard_columns(),
    Column('employee_id', Integer, ForeignKey('employees.id'), nullable=False),
    Column('questionnaire_id', Integer, ForeignKey('questionnaires.id')),
)


def start_mappers():
    departments_mapper = mapper(Department, departments)
    employees_mapper = mapper(Employee, employees, properties={
        'employee': relationship(departments_mapper)
    })
    symptoms_mapper = mapper(Symptom, symptoms)
    questionnaires_mapper = mapper(Questionnaire, questionnaires, properties={
        'symptom': relationship(symptoms_mapper)
    })
    mapper(Screening, screenings, properties={
        'employee': relationship(employees_mapper),
        'questionnaire': relationship(questionnaires_mapper),
    })
