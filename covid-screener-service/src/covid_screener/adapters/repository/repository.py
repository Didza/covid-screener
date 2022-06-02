import abc
from covid_screener.domain.model.base_model import BaseModel


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, entity: BaseModel):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, identifier) -> BaseModel:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, entity):
        self.session.add(entity)

    @abc.abstractmethod
    def get(self, identifier) -> BaseModel:
        raise NotImplementedError
