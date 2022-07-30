from covid_screener.adapters.orm import orm
from covid_screener.domain.commands.commands import CreateDepartment, \
    UpdateDepartment, CreateScreening, CreateEmployee, UpdateEmployee, \
    LoadDepartments, LoadEmployees, LoadScreenings
from covid_screener.domain.exceptions.exceptions import VaccinationException, \
    ValidationError
from covid_screener.service.services import create_department, \
    load_departments, edit_department, create_employee, load_employees, \
    edit_employee, create_screening, load_screenings
from covid_screener.service.unit_of_work import SqlAlchemyUnitOfWork
from flask import Flask, request
from pydantic import ValidationError as PydanticValidationError

app = Flask(__name__)
orm.start_mappers()


@app.route("/", methods=['GET'])
def get_hello():
    return 'Hello, from Covid Screener', 200


@app.route("/department", methods=['POST'])
def add_department():
    cmd = CreateDepartment(**request.json)
    result = create_department(cmd, SqlAlchemyUnitOfWork())
    return result, 201


@app.route("/department", methods=['PUT'])
def update_department():
    cmd = UpdateDepartment(**request.json)
    result = edit_department(cmd, SqlAlchemyUnitOfWork())
    return result, 201


@app.route("/department", methods=['GET'])
def get_departments():
    query = LoadDepartments(**request.json)
    result = load_departments(query, SqlAlchemyUnitOfWork())
    return result, 200


@app.route("/employee", methods=['POST'])
def add_employee():
    cmd = CreateEmployee(**request.json)
    result = create_employee(cmd, SqlAlchemyUnitOfWork())
    return result, 201


@app.route("/employee", methods=['PUT'])
def update_employee():
    cmd = UpdateEmployee(**request.json)
    result = edit_employee(cmd, SqlAlchemyUnitOfWork())
    return result, 201


@app.route("/employee", methods=['GET'])
def get_employees():
    query = LoadEmployees(**request.json)
    result = load_employees(query, SqlAlchemyUnitOfWork())
    return result, 200


@app.route("/screening", methods=['POST'])
def add_screening():
    cmd = CreateScreening(**request.json)
    result = create_screening(cmd, SqlAlchemyUnitOfWork())
    return result, 201


@app.route("/screening", methods=['GET'])
def get_screenings():
    query = LoadScreenings(**request.json)
    result = load_screenings(query, SqlAlchemyUnitOfWork())
    return result, 200


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, VaccinationException) or isinstance(e, ValidationError) \
            or isinstance(e, PydanticValidationError):
        return {"error": str(e)}, 400
    return {"error": "Sorry, something went wrong"}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=16006)
