import pytest
from covid_screener.domain.exceptions.exceptions import VaccinationException
from covid_screener.domain.model.screening import Symptom, Questionnaire, \
    Department, Employee, Screening


@pytest.fixture
def no_covid_symptoms() -> Symptom:
    return Symptom(has_fever=False, has_cough=False,
                   has_shortness_of_breath=False, has_fatigue=False,
                   has_body_aches=False, has_loss_of_taste=False,
                   has_loss_of_smell=False, has_sore_throat=False,
                   has_runny_nose=False, has_nausea=False,
                   is_vomiting=False, has_diarrhea=False)


@pytest.fixture
def has_covid_symptoms() -> Symptom:
    return Symptom(has_fever=True, has_cough=False,
                   has_shortness_of_breath=False, has_fatigue=True,
                   has_body_aches=False, has_loss_of_taste=False,
                   has_loss_of_smell=True, has_sore_throat=False,
                   has_runny_nose=False, has_nausea=False,
                   is_vomiting=False, has_diarrhea=False)


@pytest.fixture
def has_covid_screening(has_covid_symptoms) -> Screening:
    questionnaire = Questionnaire(symptom=has_covid_symptoms,
                                  has_tested_positive=True,
                                  awaiting_test_results=False,
                                  positive_in_last_fortnight=False,
                                  is_vaccinated=True)
    department = Department(name='IT')
    employee = Employee(username='didzazw', name='Delan',
                        surname='Musiyiwa', email='delantendai@yahoo.com',
                        department=department, is_admin=False)
    return Screening(employee=employee, questionnaire=questionnaire)


@pytest.fixture
def has_symptoms_only_screening(has_covid_symptoms) -> Screening:
    questionnaire = Questionnaire(symptom=has_covid_symptoms,
                                  has_tested_positive=False,
                                  awaiting_test_results=False,
                                  positive_in_last_fortnight=False,
                                  is_vaccinated=True)
    department = Department(name='IT')
    employee = Employee(username='didzazw', name='Delan',
                        surname='Musiyiwa', email='delantendai@yahoo.com',
                        department=department, is_admin=False)
    return Screening(employee=employee, questionnaire=questionnaire)


@pytest.fixture
def no_covid_screening(no_covid_symptoms) -> Screening:
    questionnaire = Questionnaire(symptom=no_covid_symptoms,
                                  has_tested_positive=False,
                                  awaiting_test_results=False,
                                  positive_in_last_fortnight=False,
                                  is_vaccinated=True)
    department = Department(name='IT')
    employee = Employee(username='didzazw', name='Delan',
                        surname='Musiyiwa', email='delantendai@yahoo.com',
                        department=department, is_admin=False)
    return Screening(employee=employee, questionnaire=questionnaire)


@pytest.fixture
def not_vaccinated(no_covid_symptoms) -> (Employee, Questionnaire):
    questionnaire = Questionnaire(symptom=no_covid_symptoms,
                                  has_tested_positive=False,
                                  awaiting_test_results=False,
                                  positive_in_last_fortnight=False,
                                  is_vaccinated=False)
    department = Department(name='IT')
    employee = Employee(username='didzazw', name='Delan',
                        surname='Musiyiwa', email='delantendai@yahoo.com',
                        department=department, is_admin=False)
    return employee, questionnaire


class TestScreening:
    def test_raises_exception_when_not_vaccinated(self, not_vaccinated):
        with pytest.raises(VaccinationException,
                           match=f'Hi Delan, you are '
                                 f'required to be vaccinated by HR.'):
            employee, questionnaire = not_vaccinated
            Screening(employee=employee, questionnaire=questionnaire)

    def test_screening_can_flag_a_positive(self, has_covid_screening):
        assert has_covid_screening.is_covid_positive()

    def test_screening_can_flag_symptoms(self, has_symptoms_only_screening):
        assert has_symptoms_only_screening.has_covid_symptoms()

    def test_correct_message_for_covid_positive(self, has_covid_screening):
        message = f'We wish you a speedy recovery and we advise you ' \
                  f'take the next 2 weeks to rest and recover.'
        assert has_covid_screening.get_screening_message() == message

    def test_correct_symptomatic_message(self, has_symptoms_only_screening):
        message = f'In the best efforts to keep you and all our ' \
                  f'colleagues in the IT ' \
                  f'department safe, we recommend you to take a covid ' \
                  f'test since you have been experiencing symptoms'
        assert has_symptoms_only_screening.get_screening_message() == message

    def test_correct_asymptomatic_message(self, no_covid_screening):
        message = f'Thank you for taking your screening today ' \
                  f'Delan, stay safe!'
        assert no_covid_screening.get_screening_message() == message
