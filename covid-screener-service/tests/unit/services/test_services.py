from uuid import UUID

from covid_screener.adapters.repository import repository
from covid_screener.domain.model.base_model import BaseModel
from covid_screener.domain.model.screening import Department, Employee, \
    Symptom, Questionnaire, Screening
from covid_screener.service import unit_of_work
from covid_screener.service.services import create_department, edit_department, \
    load_departments, create_employee, edit_employee, load_employees, \
    create_screening, load_screenings

default_department = Department(name="HR")
default_employee = Employee(username='tindo', name='Tindo',
                            surname='Musiyiwa',
                            email='tindo@yahoo.com',
                            department=
                            default_department,
                            is_admin=False)
symptom = Symptom(has_fever=False, has_cough=True,
                  has_shortness_of_breath=False, has_fatigue=False,
                  has_body_aches=False, has_loss_of_taste=False,
                  has_loss_of_smell=False, has_sore_throat=False,
                  has_runny_nose=False, has_nausea=False,
                  is_vomiting=False, has_diarrhea=False)
questionnaire = Questionnaire(symptom=symptom,
                              has_tested_positive=False,
                              awaiting_test_results=False,
                              positive_in_last_fortnight=False,
                              is_vaccinated=True)
screening = Screening(employee=default_employee, questionnaire=questionnaire)


class FakeRepository(repository.AbstractRepository):
    def __init__(self, model):
        self._model = set(model)

    def add(self, entity):
        self._model.add(entity)

    def get(self, identifier: UUID) -> BaseModel:
        return next(b for b in self._model if b.uuid == identifier)

    def load_all(self):
        return list(self._model)

    def get_by_email(self, email: str):
        return next((x for x in self._model if x.email == email), None)

    def get_by_name(self, name: str):
        return next((x for x in self._model if x.name == name), None)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):

    def __init__(self):
        self.departments = FakeRepository([default_department])
        self.employees = FakeRepository([default_employee])
        self.symptoms = FakeRepository([])
        self.questions = FakeRepository([])
        self.screenings = FakeRepository([screening])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


class TestService:
    def test_create_department(self):
        uow = FakeUnitOfWork()
        department_uuid = create_department(name="IT", uow=uow)
        assert department_uuid is not None
        assert uow.committed

    def test_edit_department(self):
        uow = FakeUnitOfWork()
        department_uuid = edit_department(default_department.uuid, "IT", uow)
        assert department_uuid is not None
        assert uow.committed

    def test_load_all_departments(self):
        uow = FakeUnitOfWork()
        departments = load_departments(uow)
        assert len(departments) == 1

    def test_create_employee(self):
        uow = FakeUnitOfWork()
        employee_uuid = create_employee(username='didzazw', name='Delan',
                                        surname='Musiyiwa',
                                        email='delantendai@yahoo.com',
                                        department_uuid=
                                        default_department.uuid,
                                        is_admin=False, uow=uow)
        assert employee_uuid is not None
        assert uow.committed

    def test_edit_employee(self):
        uow = FakeUnitOfWork()
        employee_uuid = edit_employee(employee_uuid=default_employee.uuid,
                                      department_uuid=None,
                                      name="Tendai", surname=None, uow=uow)
        assert employee_uuid is not None
        assert uow.committed

    def test_load_all_employees(self):
        uow = FakeUnitOfWork()
        employees = load_employees(uow)
        assert len(employees) == 1

    def test_create_screening(self):
        uow = FakeUnitOfWork()
        screening_uuid = create_screening(has_fever=False, has_cough=True,
                                          has_shortness_of_breath=False,
                                          has_fatigue=False,
                                          has_body_aches=False,
                                          has_loss_of_taste=False,
                                          has_loss_of_smell=False,
                                          has_sore_throat=False,
                                          has_runny_nose=False,
                                          has_nausea=False,
                                          is_vomiting=False,
                                          has_diarrhea=False,
                                          has_tested_positive=False,
                                          awaiting_test_results=False,
                                          positive_in_last_fortnight=False,
                                          is_vaccinated=True,
                                          employee_uuid=default_employee.uuid,
                                          uow=uow)
        assert screening_uuid is not None
        assert uow.committed

    def test_load_all_screenings(self):
        uow = FakeUnitOfWork()
        screenings = load_screenings(uow)
        assert len(screenings) == 1
