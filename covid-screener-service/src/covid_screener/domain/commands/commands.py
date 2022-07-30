from typing import Optional
from uuid import UUID

from pydantic import BaseModel, constr


class Command(BaseModel):
    pass


class Query(BaseModel):
    pass


class CreateDepartment(Command):
    name: constr(max_length=100)


class UpdateDepartment(Command):
    department_uuid: UUID
    name: constr(max_length=100)


class LoadDepartments(Query):
    pass


class CreateEmployee(Command):
    username: constr(max_length=100)
    name: constr(max_length=100)
    surname: constr(max_length=100)
    email: constr(max_length=100)
    department_uuid: UUID
    is_admin: bool


class UpdateEmployee(Command):
    employee_uuid: UUID
    department_uuid: Optional[UUID]
    name: Optional[constr(max_length=100)]
    surname: Optional[constr(max_length=100)]


class LoadEmployees(Query):
    pass


class CreateScreening(Command):
    has_fever: bool
    has_cough: bool
    has_shortness_of_breath: bool
    has_fatigue: bool
    has_body_aches: bool
    has_loss_of_taste: bool
    has_loss_of_smell: bool
    has_sore_throat: bool
    has_runny_nose: bool
    has_nausea: bool
    is_vomiting: bool
    has_diarrhea: bool
    has_tested_positive: bool
    awaiting_test_results: bool
    positive_in_last_fortnight: bool
    is_vaccinated: bool
    employee_uuid: UUID


class LoadScreenings(Query):
    pass
