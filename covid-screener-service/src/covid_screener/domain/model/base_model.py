from datetime import datetime
import uuid as uuid_generator
from uuid import UUID


class BaseModel:
    def __init__(self, uuid: UUID = None, is_active: bool = True):
        self.uuid = uuid_generator.uuid4() if uuid is None else uuid
        self.is_active = is_active
        self.created = datetime.utcnow()
        self.modified = datetime.utcnow()
