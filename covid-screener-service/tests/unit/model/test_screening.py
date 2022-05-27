from datetime import datetime

import pytest
from covid_screener.domain.model.screening import Symptom, Questionnaire


@pytest.fixture
def no_covid_symptoms() -> Symptom:
    return Symptom(has_fever=False, has_cough=False,
                   has_shortness_of_breath=False, has_fatigue=False,
                   has_body_aches=False, has_loss_of_taste=False,
                   has_loss_of_smell=False, has_sore_throat=False,
                   has_runny_nose=False, has_nausea=False,
                   is_vomiting=False, has_diarrhea=False)


class TestScreening:
    def test_screening_can_flag_a_positive(self, no_covid_symptoms):
        questionnaire = Questionnaire(symptom=no_covid_symptoms,
                                      has_tested_positive=True,
                                      awaiting_test_results=False,
                                      last_test_date=datetime(2022, 1, 23)
                                      )
