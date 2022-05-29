import uuid

from covid_screener.adapters.orm.type_decorators.guid import GUID
from sqlalchemy import (
    Column, Integer, DateTime,
    Boolean, func
)


def get_standard_columns():
    return [Column("id", Integer, primary_key=True),
            Column("is_active", Boolean, nullable=False, index=True,
                   default=True),
            Column("uuid", GUID, unique=True,
                   nullable=False, default=uuid.uuid4),
            Column("created", DateTime, nullable=False, default=func.now()),
            Column("modified", DateTime, nullable=False, default=func.now(),
                   onupdate=func.now())]