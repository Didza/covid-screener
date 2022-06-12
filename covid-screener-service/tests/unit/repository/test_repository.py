from covid_screener.adapters.repository import repository
from covid_screener.domain.model.screening import Department, Employee, \
    Screening, Questionnaire, Symptom


class TestRepository:
    def test_repo_can_save_and_retrieve_a_department(self, session):
        department = Department(name='IT')
        repo = repository.DepartmentRepository(session, Department)
        repo.add(department)

        assert repo.get(department.uuid) == department

    def test_repo_can_load_department_by_name(self, session):
        department = Department(name='IT')
        repo = repository.DepartmentRepository(session, Department)
        repo.add(department)

        assert repo.get_by_name('IT') == department

    def test_repo_can_load_all_departments(self, session):
        it_department = Department(name='IT')
        hr_department = Department(name='HR')
        repo = repository.DepartmentRepository(session, Department)
        repo.add(it_department)
        repo.add(hr_department)

        departments = repo.load_all()
        assert len(departments) == 2

    def test_repo_can_save_and_retrieve_an_employee(self, session):
        department = Department(name='IT')
        employee = Employee(username='didzazw', name='Delan',
                            surname='Musiyiwa', email='delantendai@yahoo.com',
                            department=department, is_admin=False)
        repo = repository.EmployeeRepository(session, Employee)
        repo.add(employee)

        assert repo.get(employee.uuid) == employee

    def test_repo_can_load_employee_by_email(self, session):
        department = Department(name='IT')
        employee = Employee(username='didzazw', name='Delan',
                            surname='Musiyiwa', email='delantendai@yahoo.com',
                            department=department, is_admin=False)
        repo = repository.EmployeeRepository(session, Employee)
        repo.add(employee)

        assert repo.get_by_email('delantendai@yahoo.com') == employee

    def test_repo_can_load_all_employees(self, session):
        department = Department(name='IT')
        employee_1 = Employee(username='didzazw', name='Delan',
                              surname='Musiyiwa',
                              email='delantendai@yahoo.com',
                              department=department, is_admin=False)
        employee_2 = Employee(username='teams', name='Test Name',
                              surname='Test Surname', email='test@yahoo.com',
                              department=department, is_admin=False)
        repo = repository.EmployeeRepository(session, Employee)
        repo.add(employee_1)
        repo.add(employee_2)

        departments = repo.load_all()
        assert len(departments) == 2

    def test_repo_can_save_and_retrieve_an_screenings(self, session):
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
                            surname='Musiyiwa', email='delantendai@yahoo.com',
                            department=department, is_admin=False)

        screening = Screening(employee=employee, questionnaire=questionnaire)
        repo = repository.ScreeningRepository(session, Screening)
        repo.add(screening)

        assert repo.get(screening.uuid) == screening
