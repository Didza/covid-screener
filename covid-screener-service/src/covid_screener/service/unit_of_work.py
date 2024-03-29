from __future__ import annotations
import abc

from covid_screener.adapters.repository.repository import AbstractRepository, \
    DepartmentRepository, SymptomRepository, QuestionnaireRepository, \
    ScreeningRepository, EmployeeRepository
from covid_screener.config import config
from covid_screener.domain.model.screening import Department, Symptom, \
    Questionnaire, Screening, Employee
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


class AbstractUnitOfWork(abc.ABC):
    departments: AbstractRepository
    employees: AbstractRepository
    symptoms: AbstractRepository
    questions: AbstractRepository
    screenings: AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(bind=create_engine(
    config.get_postgres_uri(),
))


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):

    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.departments = DepartmentRepository(self.session, Department)
        self.employees = EmployeeRepository(self.session, Employee)
        self.symptoms = SymptomRepository(self.session, Symptom)
        self.questions = QuestionnaireRepository(self.session, Questionnaire)
        self.screenings = ScreeningRepository(self.session, Screening)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
