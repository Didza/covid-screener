import uuid
from datetime import datetime

from covid_screener.domain.exceptions.exceptions import ValidationError
from covid_screener.domain.model.screening import Questionnaire, Symptom, \
    Screening, Department, Employee
from covid_screener.service.unit_of_work import SqlAlchemyUnitOfWork


class TestUow:
    def test_uow_can_add_and_get_screenings(self, sqlite_session_factory):
        uow = SqlAlchemyUnitOfWork(sqlite_session_factory)
        with uow:
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
            department = Department(name='IT')
            employee = Employee(username='didzazw', name='Delan',
                                surname='Musiyiwa',
                                email='delantendai@yahoo.com',
                                department=department, is_admin=False)
            screening = Screening(employee, questionnaire)
            uow.screenings.add(screening)
            uow.commit()
            result = uow.screenings.load_all()
            assert result != 0
