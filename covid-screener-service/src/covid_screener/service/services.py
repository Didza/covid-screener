from uuid import UUID

from covid_screener.domain.exceptions.exceptions import ValidationError
from covid_screener.domain.model.screening import Department
from covid_screener.service.unit_of_work import AbstractUnitOfWork


def create_department(name: str, uow: AbstractUnitOfWork):
    with uow:
        department = uow.department.get_by_name(name)
        if not department:
            department = Department(name)
            uow.department.add(department)
            uow.commit()
        return str(department.uuid)


def edit_department(department_uuid: UUID, name: str, uow: AbstractUnitOfWork):
    with uow:
        department = uow.department.get(department_uuid)
        if not department:
            raise ValidationError('This department does not exist.')
        department.name = name
        uow.commit()
        return str(department.uuid)


def load_departments(uow: AbstractUnitOfWork):
    with uow:
        departments = uow.department.load_all()
        return departments
