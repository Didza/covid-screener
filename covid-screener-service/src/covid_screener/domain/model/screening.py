from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from covid_screener.domain.model.base_model import BaseModel


class Screening(BaseModel):
    def __init__(self, employee: Employee, questionnaire: Questionnaire):
        super().__init__()
        self.employee = employee
        self.questionnaire = questionnaire

    def is_covid_positive(self) -> bool:
        return self.questionnaire.has_tested_positive

    def has_covid_symptoms(self) -> bool:
        return self.questionnaire.symptom.has_covid_symptom()

    def get_screening_message(self) -> str:
        message = f'Thank you for taking your screening today ' \
                  f'{self.employee.name}, stay safe!'
        if self.is_covid_positive():
            message = f'We wish you a speedy recovery and we advise you ' \
                      f'take the next 2 weeks to rest and recover.'
        elif self.has_covid_symptoms():
            message = f'In the best efforts to keep you and all our ' \
                      f'colleagues in the {self.employee.department.name} ' \
                      f'department safe, we recommend you to take a covid ' \
                      f'test since you have been experiencing symptoms'
        return message


class Questionnaire(BaseModel):
    def __init__(self, symptom: Symptom, has_tested_positive: bool,
                 awaiting_test_results: bool,
                 positive_in_last_fortnight: bool,
                 last_test_date: Optional[datetime]):
        super().__init__()
        self.symptom = symptom
        self.has_tested_positive = has_tested_positive
        self.awaiting_test_results = awaiting_test_results
        self.positive_in_last_fortnight = positive_in_last_fortnight
        self.last_test_date = last_test_date


@dataclass(unsafe_hash=True)
class Symptom:
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

    def has_covid_symptom(self):
        return True if self.has_fever or self.has_cough or \
                       self.has_fatigue or self.has_shortness_of_breath or \
                       self.has_body_aches or self.has_loss_of_taste or \
                       self.has_loss_of_smell or self.has_sore_throat or \
                       self.has_runny_nose or self.has_nausea or \
                       self.is_vomiting or self.has_diarrhea else False


class Employee(BaseModel):
    def __init__(self, username: str, name: str, surname: str, email: str,
                 department: Department, is_admin: bool):
        super().__init__()
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        self.department = department
        self.is_admin = is_admin


class Department(BaseModel):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
