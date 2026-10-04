from enum import Enum
from pydantic import BaseModel


class EventType(Enum):
    MODIFIED = "modified"
    DELETED = "deleted"
    MOVED = "moved"


class Event(BaseModel):
    src_path: str
    event_type: EventType
    dest_path: str | None = None


class File(BaseModel):
    id: str
    path: str
    content_hash: str
