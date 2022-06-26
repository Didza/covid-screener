from uuid import UUID

from covid_screener.adapters.orm import orm
from covid_screener.service.services import create_department, \
    load_departments, edit_department, create_employee, load_employees, \
    edit_employee
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=16006)
