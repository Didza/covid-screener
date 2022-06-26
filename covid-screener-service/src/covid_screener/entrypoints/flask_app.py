from uuid import UUID

from covid_screener.adapters.orm import orm
from covid_screener.domain.exceptions.exceptions import VaccinationException, \
    ValidationError
from covid_screener.service.services import create_department, \
    load_departments, edit_department, create_employee, load_employees, \
    edit_employee, create_screening, load_screenings
from covid_screener.service.unit_of_work import SqlAlchemyUnitOfWork
from flask import Flask, request

app = Flask(__name__)
orm.start_mappers()


@app.route("/", methods=['GET'])
def get_hello():
    return 'Hello, from Covid Screener', 200


@app.route("/department", methods=['POST'])
def add_department():
    name = request.json['name']
    result = create_department(name, SqlAlchemyUnitOfWork())
    return result, 201


@app.route("/department", methods=['PUT'])
def update_department():
    department_uuid = UUID(request.json['department_uuid'])
    name = request.json.get('name')
    result = edit_department(department_uuid, name, SqlAlchemyUnitOfWork())
    return result, 201


@app.route("/department", methods=['GET'])
def get_departments():
    result = load_departments(SqlAlchemyUnitOfWork())
    return result, 200


@app.route("/employee", methods=['POST'])
def add_employee():
    username = request.json['username']
    name = request.json['name']
    surname = request.json['surname']
    email = request.json['email']
    department_uuid = UUID(request.json['department_uuid'])
    is_admin = request.json['is_admin']
    result = create_employee(username, name, surname, email, department_uuid,
                             is_admin, SqlAlchemyUnitOfWork())
    return result, 201


@app.route("/employee", methods=['PUT'])
def update_employee():
    employee_uuid = UUID(request.json['employee_uuid'])
    department_uuid = request.json.get('department_uuid')
    if department_uuid:
        department_uuid = UUID(department_uuid)
    name = request.json.get('name')
    surname = request.json.get('surname')
    result = edit_employee(employee_uuid, department_uuid, name, surname,
                           SqlAlchemyUnitOfWork())
    return result, 201


@app.route("/employee", methods=['GET'])
def get_employees():
    result = load_employees(SqlAlchemyUnitOfWork())
    return result, 200


@app.route("/screening", methods=['POST'])
def add_screening():
    has_fever = request.json['has_fever']
    has_cough = request.json['has_cough']
    has_shortness_of_breath = request.json['has_shortness_of_breath']
    has_fatigue = request.json['has_fatigue']
    has_body_aches = request.json['has_body_aches']
    has_loss_of_taste = request.json['has_loss_of_taste']
    has_loss_of_smell = request.json['has_loss_of_smell']
    has_sore_throat = request.json['has_sore_throat']
    has_runny_nose = request.json['has_runny_nose']
    has_nausea = request.json['has_nausea']
    is_vomiting = request.json['is_vomiting']
    has_diarrhea = request.json['has_diarrhea']
    has_tested_positive = request.json['has_tested_positive']
    awaiting_test_results = request.json['awaiting_test_results']
    positive_in_last_fortnight = request.json['positive_in_last_fortnight']
    is_vaccinated = request.json['is_vaccinated']
    employee_uuid = UUID(request.json['employee_uuid'])
    result = create_screening(has_fever, has_cough, has_shortness_of_breath,
                              has_fatigue, has_body_aches, has_loss_of_taste,
                              has_loss_of_smell, has_sore_throat,
                              has_runny_nose, has_nausea, is_vomiting,
                              has_diarrhea, has_tested_positive,
                              awaiting_test_results,
                              positive_in_last_fortnight,
                              is_vaccinated, employee_uuid,
                              SqlAlchemyUnitOfWork())
    return result, 201


@app.route("/screening", methods=['GET'])
def get_screenings():
    result = load_screenings(SqlAlchemyUnitOfWork())
    return result, 200


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, VaccinationException) or isinstance(e, ValidationError):
        return {"error": str(e)}, 400
    return {"error": "Sorry, something went wrong"}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=16006)
