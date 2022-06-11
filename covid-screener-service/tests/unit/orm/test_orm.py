from datetime import datetime

from covid_screener.domain.model.screening import Department, Employee, \
    Symptom, Questionnaire, Screening
import uuid


class TestOrm:
    def test_departments_mapper_can_load_departments(self, session):
        session.execute(
            'INSERT INTO departments(is_active, uuid, created, modified, name)'
            'VALUES(:is_active, :uuid, :created, :modified, :name)',
            dict(is_active=True, uuid=str(uuid.uuid4()),
                 created=datetime.now(), modified=datetime.now(), name='IT'),
        )
        session.execute(
            'INSERT INTO departments(is_active, uuid, created, modified, name)'
            'VALUES(:is_active, :uuid, :created, :modified, :name)',
            dict(is_active=True, uuid=str(uuid.uuid4()),
                 created=datetime.now(), modified=datetime.now(), name='HR'),
        )

        expected = [Department(name='IT'), Department(name='HR')]
        assert session.query(Department).all() == expected

    def test_departments_mapper_can_save_departments(self, session):
        department = Department("IT")
        session.add(department)
        session.commit()

        rows = list(session.execute('SELECT name FROM "departments"'))
        assert rows == [('IT',)]

    def test_employees_mapper_can_load_employees(self, session):
        session.execute(
            'INSERT INTO departments(is_active, uuid, created, modified, name)'
            'VALUES(:is_active, :uuid, :created, :modified, :name)',
            dict(is_active=True, uuid=str(uuid.uuid4()),
                 created=datetime.now(), modified=datetime.now(), name='IT'),
        )
        [[department_id]] = session.execute(
            'SELECT id FROM departments WHERE name=:name',
            dict(name='IT')
        )
        session.execute(
            'INSERT INTO employees(is_active, uuid, created, modified, '
            'username, name, surname, email, department_id, is_admin)'
            'VALUES(:is_active, :uuid, :created, :modified, :username, '
            ':name, :surname, :email, :department_id, :is_admin)',
            dict(is_active=True, uuid=str(uuid.uuid4()),
                 created=datetime.now(), modified=datetime.now(),
                 username='didzazw', name='Delan', surname='Musiyiwa',
                 email='delantendai@yahoo.com', department_id=department_id,
                 is_admin=False),
        )

        department = Department(name='IT')
        expected = [Employee(username='didzazw', name='Delan',
                             surname='Musiyiwa', email='delantendai@yahoo.com',
                             department=department, is_admin=False)]
        assert session.query(Employee).all() == expected

    def test_employees_mapper_can_save_employees(self, session):
        department = Department(name='IT')
        employee = Employee(username='didzazw', name='Delan',
                            surname='Musiyiwa', email='delantendai@yahoo.com',
                            department=department, is_admin=False)
        session.add(employee)
        session.commit()

        rows = list(session.execute('SELECT username, email FROM employees'))
        assert rows == [('didzazw', 'delantendai@yahoo.com')]

    def test_symptoms_mapper_can_load_symptoms(self, session):
        session.execute(
            'INSERT INTO symptoms(is_active, uuid, created, modified, '
            'has_fever, has_cough, has_shortness_of_breath, has_fatigue,'
            'has_body_aches, has_loss_of_taste, has_loss_of_smell, '
            'has_sore_throat, has_runny_nose, has_nausea, is_vomiting, '
            'has_diarrhea)'
            'VALUES(:is_active, :uuid, :created, :modified, :has_fever,  '
            ':has_cough, :has_shortness_of_breath, :has_fatigue, '
            ':has_body_aches, :has_loss_of_taste, :has_loss_of_smell, '
            ':has_sore_throat, :has_runny_nose, :has_nausea, :is_vomiting, '
            ':has_diarrhea)',
            dict(is_active=True, uuid=str(uuid.uuid4()),
                 created=datetime.now(), modified=datetime.now(),
                 has_fever=False, has_cough=True,
                 has_shortness_of_breath=False, has_fatigue=False,
                 has_body_aches=False, has_loss_of_taste=False,
                 has_loss_of_smell=False, has_sore_throat=False,
                 has_runny_nose=False, has_nausea=False, is_vomiting=False,
                 has_diarrhea=False),
        )

        expected = [Symptom(has_fever=False, has_cough=True,
                            has_shortness_of_breath=False, has_fatigue=False,
                            has_body_aches=False, has_loss_of_taste=False,
                            has_loss_of_smell=False, has_sore_throat=False,
                            has_runny_nose=False, has_nausea=False,
                            is_vomiting=False, has_diarrhea=False)]
        assert session.query(Symptom).all() == expected

    def test_symptoms_mapper_can_save_symptoms(self, session):
        symptom = Symptom(has_fever=True, has_cough=False,
                          has_shortness_of_breath=True, has_fatigue=False,
                          has_body_aches=False, has_loss_of_taste=False,
                          has_loss_of_smell=False, has_sore_throat=False,
                          has_runny_nose=False, has_nausea=False,
                          is_vomiting=False, has_diarrhea=False)
        session.add(symptom)
        session.commit()

        rows = list(session.execute('SELECT has_fever, has_cough, '
                                    'has_shortness_of_breath '
                                    'FROM symptoms'))
        assert rows == [(True, False, True)]

    def test_questionnaires_mapper_can_load_questionnaires(self, session):
        session.execute(
            'INSERT INTO symptoms(is_active, uuid, created, modified, '
            'has_fever, has_cough, has_shortness_of_breath, has_fatigue,'
            'has_body_aches, has_loss_of_taste, has_loss_of_smell, '
            'has_sore_throat, has_runny_nose, has_nausea, is_vomiting, '
            'has_diarrhea)'
            'VALUES(:is_active, :uuid, :created, :modified, :has_fever,  '
            ':has_cough, :has_shortness_of_breath, :has_fatigue, '
            ':has_body_aches, :has_loss_of_taste, :has_loss_of_smell, '
            ':has_sore_throat, :has_runny_nose, :has_nausea, :is_vomiting, '
            ':has_diarrhea)',
            dict(is_active=True, uuid=str(uuid.uuid4()),
                 created=datetime.now(), modified=datetime.now(),
                 has_fever=False, has_cough=True,
                 has_shortness_of_breath=False, has_fatigue=False,
                 has_body_aches=False, has_loss_of_taste=False,
                 has_loss_of_smell=False, has_sore_throat=False,
                 has_runny_nose=False, has_nausea=False, is_vomiting=False,
                 has_diarrhea=False),
        )

        [[symptom_id]] = session.execute(
            'SELECT id FROM symptoms '
        )

        session.execute(
            'INSERT INTO questionnaires(is_active, uuid, created, modified, '
            'has_tested_positive, awaiting_test_results, '
            'positive_in_last_fortnight, is_vaccinated, symptom_id)'
            'VALUES(:is_active, :uuid, :created, :modified, '
            ':has_tested_positive, :awaiting_test_results, '
            ':positive_in_last_fortnight, :is_vaccinated, :symptom_id)',
            dict(is_active=True, uuid=str(uuid.uuid4()),
                 created=datetime.now(), modified=datetime.now(),
                 has_tested_positive=False, awaiting_test_results=False,
                 positive_in_last_fortnight=False, is_vaccinated=True,
                 symptom_id=symptom_id),
        )

        symptom = Symptom(has_fever=False, has_cough=True,
                          has_shortness_of_breath=False, has_fatigue=False,
                          has_body_aches=False, has_loss_of_taste=False,
                          has_loss_of_smell=False, has_sore_throat=False,
                          has_runny_nose=False, has_nausea=False,
                          is_vomiting=False, has_diarrhea=False)
        expected = [Questionnaire(symptom=symptom,
                                  has_tested_positive=False,
                                  awaiting_test_results=False,
                                  positive_in_last_fortnight=False,
                                  is_vaccinated=True)]
        assert session.query(Questionnaire).all() == expected

    def test_questionnaires_mapper_can_save_questionnaires(self, session):
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
        session.add(questionnaire)
        session.commit()

        rows = list(session.execute('SELECT has_tested_positive, '
                                    'awaiting_test_results,'
                                    'is_vaccinated '
                                    'FROM questionnaires'))
        assert rows == [(False, False, True)]

    def test_screenings_mapper_can_load_screenings(self, session):
        session.execute(
            'INSERT INTO symptoms(is_active, uuid, created, modified, '
            'has_fever, has_cough, has_shortness_of_breath, has_fatigue,'
            'has_body_aches, has_loss_of_taste, has_loss_of_smell, '
            'has_sore_throat, has_runny_nose, has_nausea, is_vomiting, '
            'has_diarrhea)'
            'VALUES(:is_active, :uuid, :created, :modified, :has_fever,  '
            ':has_cough, :has_shortness_of_breath, :has_fatigue, '
            ':has_body_aches, :has_loss_of_taste, :has_loss_of_smell, '
            ':has_sore_throat, :has_runny_nose, :has_nausea, :is_vomiting, '
            ':has_diarrhea)',
            dict(is_active=True, uuid=str(uuid.uuid4()),
                 created=datetime.now(), modified=datetime.now(),
                 has_fever=False, has_cough=True,
                 has_shortness_of_breath=False, has_fatigue=False,
                 has_body_aches=False, has_loss_of_taste=False,
                 has_loss_of_smell=False, has_sore_throat=False,
                 has_runny_nose=False, has_nausea=False, is_vomiting=False,
                 has_diarrhea=False),
        )

        [[symptom_id]] = session.execute(
            'SELECT id FROM symptoms '
        )
        questionnaires_uuid = uuid.uuid4()
        session.execute(
            'INSERT INTO questionnaires(is_active, uuid, created, modified, '
            'has_tested_positive, awaiting_test_results, '
            'positive_in_last_fortnight, is_vaccinated, symptom_id)'
            'VALUES(:is_active, :uuid, :created, :modified, '
            ':has_tested_positive, :awaiting_test_results, '
            ':positive_in_last_fortnight, :is_vaccinated, :symptom_id)',
            dict(is_active=True, uuid=str(questionnaires_uuid),
                 created=datetime.now(), modified=datetime.now(),
                 has_tested_positive=False, awaiting_test_results=False,
                 positive_in_last_fortnight=False, is_vaccinated=True,
                 symptom_id=symptom_id),
        )

        [[questionnaire_id]] = session.execute(
            'SELECT id FROM questionnaires WHERE uuid=:uuid ',
            dict(uuid=str(questionnaires_uuid))
        )

        session.execute(
            'INSERT INTO departments(is_active, uuid, created, modified, name)'
            'VALUES(:is_active, :uuid, :created, :modified, :name)',
            dict(is_active=True, uuid=str(uuid.uuid4()),
                 created=datetime.now(), modified=datetime.now(), name='IT'),
        )
        [[department_id]] = session.execute(
            'SELECT id FROM departments WHERE name=:name',
            dict(name='IT')
        )
        session.execute(
            'INSERT INTO employees(is_active, uuid, created, modified, '
            'username, name, surname, email, department_id, is_admin)'
            'VALUES(:is_active, :uuid, :created, :modified, :username, '
            ':name, :surname, :email, :department_id, :is_admin)',
            dict(is_active=True, uuid=str(uuid.uuid4()),
                 created=datetime.now(), modified=datetime.now(),
                 username='didzazw', name='Delan', surname='Musiyiwa',
                 email='delantendai@yahoo.com', department_id=department_id,
                 is_admin=False),
        )

        [[employee_id]] = session.execute(
            'SELECT id FROM employees WHERE username=:username',
            dict(username='didzazw')
        )

        session.execute(
            'INSERT INTO screenings(is_active, uuid, created, modified, '
            'employee_id, questionnaire_id)'
            'VALUES(:is_active, :uuid, :created, :modified, :employee_id,'
            ':questionnaire_id)',
            dict(is_active=True, uuid=str(uuid.uuid4()),
                 created=datetime.now(), modified=datetime.now(),
                 employee_id=employee_id, questionnaire_id=questionnaire_id),
        )
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

        expected = [Screening(employee=employee, questionnaire=questionnaire)]
        assert session.query(Screening).all() == expected

    def test_screenings_mapper_can_save_screenings(self, session):
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
        session.add(screening)
        session.commit()

        rows = list(session.execute('SELECT employees.username, '
                                    'employees.name, employees.email '
                                    'FROM screenings '
                                    'JOIN employees ON employees.id == '
                                    'screenings.employee_id'))

        assert rows == [('didzazw', 'Delan', 'delantendai@yahoo.com')]
