from __future__ import annotations

import abc
from typing import Union, List, Dict, Type

from covid_screener.domain.model.base_model import BaseModel
from covid_screener.domain.model.screening import Department, Employee, \
    Screening


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


class ScreeningTransformer(AbstractTransformer):
    @staticmethod
    def _build_json(item: Screening):
        return {
            "uuid": str(item.uuid),
            "employee": {
               "uuid": str(item.employee.uuid),
               "name": item.employee.name,
            },
            "questionnaire": {
                "symptoms": {
                    "has_fever": item.questionnaire.symptom.has_fever,
                    "has_cough": item.questionnaire.symptom.has_cough,
                    "has_shortness_of_breath":
                        item.questionnaire.symptom.has_shortness_of_breath,
                    "has_fatigue": item.questionnaire.symptom.has_fatigue,
                    "has_body_aches":
                        item.questionnaire.symptom.has_body_aches,
                    "has_loss_of_taste":
                        item.questionnaire.symptom.has_loss_of_taste,
                    "has_loss_of_smell":
                        item.questionnaire.symptom.has_loss_of_smell,
                    "has_sore_throat":
                        item.questionnaire.symptom.has_sore_throat,
                    "has_runny_nose":
                        item.questionnaire.symptom.has_runny_nose,
                    "has_nausea": item.questionnaire.symptom.has_nausea,
                    "is_vomiting": item.questionnaire.symptom.is_vomiting,
                    "has_diarrhea": item.questionnaire.symptom.has_diarrhea,
                },
                "has_tested_positive": item.questionnaire.has_tested_positive,
                "awaiting_test_results":
                    item.questionnaire.awaiting_test_results,
                "positive_in_last_fortnight":
                    item.questionnaire.positive_in_last_fortnight,
                "is_vaccinated": item.questionnaire.is_vaccinated,
            },
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
    Screening: ScreeningTransformer,
}  # type: Dict[Type[BaseModel], Type[AbstractTransformer]]
