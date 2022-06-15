from uuid import UUID

from covid_screener.adapters.repository import repository
from covid_screener.domain.model.base_model import BaseModel


class FakeRepository(repository.AbstractRepository):
    def __init__(self, data):
        self._model = set(data)

    def add(self, entity):
        self._model.add(entity)

    def get(self, identifier: UUID) -> BaseModel:
        return next(b for b in self._model if b.identifier == identifier)

    def load_all(self):
        return list(self._model)


