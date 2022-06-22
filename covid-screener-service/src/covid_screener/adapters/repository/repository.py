import abc
from uuid import UUID

from covid_screener.domain.model.base_model import BaseModel


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, entity: BaseModel):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, identifier) -> BaseModel:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session, model):
        self.session = session
        self.model = model

    def add(self, entity):
        self.session.add(entity)

    def get(self, identifier: UUID) -> BaseModel:
        return self.session.query(self.model).filter_by(
            uuid=identifier).first()

    def load_all(self):
        return self.session.query(self.model).all()


class DepartmentRepository(SqlAlchemyRepository):
    def get_by_name(self, name: str):
        return self.session.query(self.model).filter_by(
            name=name).first()


class EmployeeRepository(SqlAlchemyRepository):
    def get_by_email(self, email: str):
        return self.session.query(self.model).filter_by(
            email=email).first()


class SymptomRepository(SqlAlchemyRepository):
    pass


class QuestionnaireRepository(SqlAlchemyRepository):
    pass


class ScreeningRepository(SqlAlchemyRepository):
    pass
