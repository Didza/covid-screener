from uuid import UUID

from covid_screener.adapters.repository import repository
from covid_screener.domain.model.base_model import BaseModel
from covid_screener.domain.model.screening import Department
from covid_screener.service import unit_of_work
from covid_screener.service.services import create_department, edit_department, \
    load_departments

default_department = Department(name="HR")


class FakeRepository(repository.AbstractRepository):
    def __init__(self, model):
        self._model = set(model)

    def add(self, entity):
        self._model.add(entity)

    def get(self, identifier: UUID) -> BaseModel:
        return next(b for b in self._model if b.uuid == identifier)

    def load_all(self):
        return list(self._model)

    def get_by_name(self, name: str):
        return next((x for x in self._model if x.name == name), None)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):

    def __init__(self):
        self.department = FakeRepository([default_department])
        self.symptom = FakeRepository([])
        self.question = FakeRepository([])
        self.screening = FakeRepository([])
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

