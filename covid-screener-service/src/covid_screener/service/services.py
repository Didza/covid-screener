from covid_screener.domain.commands.commands import CreateDepartment, \
    UpdateDepartment, CreateScreening, CreateEmployee, UpdateEmployee, \
    LoadDepartments, LoadEmployees, LoadScreenings
from covid_screener.domain.exceptions.exceptions import ValidationError
from covid_screener.domain.model.screening import Department, Employee, \
    Symptom, Questionnaire, Screening
from covid_screener.service.transformer import base_response
from covid_screener.service.unit_of_work import AbstractUnitOfWork


def create_department(cmd: CreateDepartment, uow: AbstractUnitOfWork):
    with uow:
        department = uow.departments.get_by_name(cmd.name)
        if not department:
            department = Department(cmd.name)
            uow.departments.add(department)
            uow.commit()
        return base_response(department)


def edit_department(cmd: UpdateDepartment, uow: AbstractUnitOfWork):
    with uow:
        department = uow.departments.get(cmd.department_uuid)
        if not department:
            raise ValidationError('This department does not exist.')
        if cmd.name:
            department.name = cmd.name
        uow.commit()
        return base_response(department)


def load_departments(query: LoadDepartments, uow: AbstractUnitOfWork):
    with uow:
        departments = uow.departments.load_all()
        return base_response(departments)


def create_employee(cmd: CreateEmployee, uow: AbstractUnitOfWork):
    with uow:
        employee = uow.employees.get_by_email(cmd.email)
        if not employee:
            department = uow.departments.get(cmd.department_uuid)
            if not department:
                raise ValidationError('This department uuid does not exist.')
            employee = Employee(cmd.username, cmd.name, cmd.surname, cmd.email,
                                department, cmd.is_admin)
            uow.employees.add(employee)
            uow.commit()
        return base_response(employee)


def edit_employee(cmd: UpdateEmployee, uow: AbstractUnitOfWork):
    with uow:
        employee = uow.employees.get(cmd.employee_uuid)
        if not employee:
            raise ValidationError('This employee does not exist.')
        if cmd.name:
            employee.name = cmd.name
        if cmd.surname:
            employee.surname = cmd.surname
        if cmd.department_uuid:
            department = uow.departments.get(cmd.department_uuid)
            if not department:
                raise ValidationError('This department uuid does not exist.')
            employee.department = department
        uow.commit()
        return base_response(employee)


def load_employees(query: LoadEmployees, uow: AbstractUnitOfWork):
    with uow:
        employees = uow.employees.load_all()
        return base_response(employees)


def create_screening(cmd: CreateScreening, uow: AbstractUnitOfWork):
    with uow:
        symptom = Symptom(cmd.has_fever, cmd.has_cough,
                          cmd.has_shortness_of_breath,
                          cmd.has_fatigue, cmd.has_body_aches,
                          cmd.has_loss_of_taste, cmd.has_loss_of_smell,
                          cmd.has_sore_throat, cmd.has_runny_nose,
                          cmd.has_nausea, cmd.is_vomiting, cmd.has_diarrhea)
        questionnaire = Questionnaire(symptom, cmd.has_tested_positive,
                                      cmd.awaiting_test_results,
                                      cmd.positive_in_last_fortnight,
                                      cmd.is_vaccinated)
        employee = uow.employees.get(cmd.employee_uuid)
        if not employee:
            raise ValidationError('This employee does not exist.')
        screening = Screening(employee, questionnaire)
        uow.screenings.add(screening)
        uow.commit()
        return base_response(screening)


def load_screenings(query: LoadScreenings, uow: AbstractUnitOfWork):
    with uow:
        screenings = uow.screenings.load_all()
        return base_response(screenings)
