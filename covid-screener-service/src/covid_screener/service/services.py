from typing import Optional
from uuid import UUID

from covid_screener.domain.exceptions.exceptions import ValidationError
from covid_screener.domain.model.screening import Department, Employee, \
    Symptom, Questionnaire, Screening
from covid_screener.service.transformer import base_response
from covid_screener.service.unit_of_work import AbstractUnitOfWork


def create_department(name: str, uow: AbstractUnitOfWork):
    with uow:
        department = uow.departments.get_by_name(name)
        if not department:
            department = Department(name)
            uow.departments.add(department)
            uow.commit()
        return base_response(department)


def edit_department(department_uuid: UUID, name: Optional[str],
                    uow: AbstractUnitOfWork):
    with uow:
        department = uow.departments.get(department_uuid)
        if not department:
            raise ValidationError('This department does not exist.')
        department.name = name
        uow.commit()
        return base_response(department)


def load_departments(uow: AbstractUnitOfWork):
    with uow:
        departments = uow.departments.load_all()
        return base_response(departments)


def create_employee(username: str, name: str, surname: str, email: str,
                    department_uuid: UUID, is_admin: bool,
                    uow: AbstractUnitOfWork):
    with uow:
        employee = uow.employees.get_by_email(email)
        if not employee:
            department = uow.departments.get(department_uuid)
            if not department:
                raise ValidationError('This department uuid does not exist.')
            employee = Employee(username, name, surname, email, department,
                                is_admin)
            uow.employees.add(employee)
            uow.commit()
        return str(employee.uuid)


def edit_employee(employee_uuid: UUID, department_uuid: Optional[UUID],
                  name: Optional[str], surname: Optional[str],
                  uow: AbstractUnitOfWork):
    with uow:
        employee = uow.employees.get(employee_uuid)
        if not employee:
            raise ValidationError('This employee does not exist.')
        if name:
            employee.name = name
        if surname:
            employee.surname = surname
        if department_uuid:
            department = uow.departments.get(department_uuid)
            if not department:
                raise ValidationError('This department uuid does not exist.')
            employee.department = department
        uow.commit()
        return str(employee.uuid)


def load_employees(uow: AbstractUnitOfWork):
    with uow:
        employees = uow.employees.load_all()
        return employees


def create_screening(has_fever: bool, has_cough: bool,
                     has_shortness_of_breath: bool, has_fatigue: bool,
                     has_body_aches: bool, has_loss_of_taste: bool,
                     has_loss_of_smell: bool, has_sore_throat: bool,
                     has_runny_nose: bool, has_nausea: bool, is_vomiting: bool,
                     has_diarrhea: bool, has_tested_positive: bool,
                     awaiting_test_results: bool,
                     positive_in_last_fortnight: bool, is_vaccinated: bool,
                     department_uuid: UUID, employee_uuid: UUID,
                     uow: AbstractUnitOfWork):
    with uow:
        symptom = Symptom(has_fever, has_cough, has_shortness_of_breath,
                          has_fatigue, has_body_aches, has_loss_of_taste,
                          has_loss_of_smell, has_sore_throat, has_runny_nose,
                          has_nausea, is_vomiting, has_diarrhea)
        questionnaire = Questionnaire(symptom, has_tested_positive,
                                      awaiting_test_results,
                                      positive_in_last_fortnight,
                                      is_vaccinated)
        department = uow.departments.get(department_uuid)
        if not department:
            raise ValidationError('This department does not exist.')
        employee = uow.employees.get(employee_uuid)
        if not employee:
            raise ValidationError('This employee does not exist.')
        screening = Screening(employee, questionnaire)
        uow.screenings.add(screening)
        uow.commit()
        return str(screening.uuid)


def load_screenings(uow: AbstractUnitOfWork):
    with uow:
        screenings = uow.screenings.load_all()
        return screenings
