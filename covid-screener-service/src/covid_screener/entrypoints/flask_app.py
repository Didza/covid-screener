from covid_screener.adapters.orm import orm
from covid_screener.service.services import create_department
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
    create_department(name, SqlAlchemyUnitOfWork())
    return 'OK', 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=16006)
