from __future__ import annotations

import abc
from typing import Union, List, Dict, Type

from covid_screener.domain.model.base_model import BaseModel
from covid_screener.domain.model.screening import Department, Employee


class AbstractTransformer(abc.ABC):
    def transform(self, data):
        return self._transform(data)

    def _transform(self, data):
        if isinstance(data, list):
            results = []
            for item in data:
                results.append(self._build_json(item))
            else:
                return {'items': results}

        return {'items': [self._build_json(data)]}

    @staticmethod
    @abc.abstractmethod
    def _build_json(item):
        raise NotImplementedError


class DepartmentTransformer(AbstractTransformer):
    @staticmethod
    def _build_json(item: Department):
        return {
            "uuid": str(item.uuid),
            "name": item.name,
            "is_active": item.is_active
        }


class EmployeeTransformer(AbstractTransformer):
    @staticmethod
    def _build_json(item: Employee):
        return {
            "uuid": str(item.uuid),
            "username": item.username,
            "name": item.name,
            "surname": item.surname,
            "email": item.email,
            "department": {
              "uuid": str(item.department.uuid),
              "name": item.department.name,
            },
            "is_admin": item.is_admin,
            "is_active": item.is_active
        }


def base_response(data: Union[BaseModel, List[BaseModel]]):
    if not data:
        return {'items': []}

    if isinstance(data, list):
        entity = data[0]
    else:
        entity = data
    return TRANSFORMERS[type(entity)]().transform(data)


TRANSFORMERS = {
    Department: DepartmentTransformer,
    Employee: EmployeeTransformer,
}  # type: Dict[Type[BaseModel], Type[AbstractTransformer]]
