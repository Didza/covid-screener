from datetime import datetime

from covid_screener.domain.model.screening import Department
import uuid


def test_departments_mapper_can_load_departments(session):
    session.execute(
        'INSERT INTO departments(is_active, uuid, created, modified, name) '
        'VALUES(:is_active, :uuid, :created, :modified, :name)',
        dict(is_active=True, uuid=str(uuid.uuid4()), created=datetime.now(),
             modified=datetime.now(), name='IT'),
    )
    session.execute(
        'INSERT INTO departments(is_active, uuid, created, modified, name) '
        'VALUES(:is_active, :uuid, :created, :modified, :name)',
        dict(is_active=True, uuid=str(uuid.uuid4()), created=datetime.now(),
             modified=datetime.now(), name='HR'),
    )
    expected = [Department(name='IT'), Department(name='HR')]

    assert session.query(Department).all() == expected
