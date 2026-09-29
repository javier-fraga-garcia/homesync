from enum import Enum
from dataclasses import dataclass


class EventType(Enum):
    MODIFIED = "modified"
    DELETED = "deleted"
    MOVED = "moved"


@dataclass
class Event:
    src_path: str
    event_type: EventType
    dest_path: str | None
