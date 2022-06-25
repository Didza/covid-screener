from covid_screener.adapters.orm import orm
from covid_screener.service.services import create_department, load_departments
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
def edit_department():
    name = request.json['name']
    create_department(name, SqlAlchemyUnitOfWork())
    return 'OK', 201


@app.route("/department", methods=['GET'])
def get_departments():
    result = load_departments(SqlAlchemyUnitOfWork())
    return result, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=16006)
