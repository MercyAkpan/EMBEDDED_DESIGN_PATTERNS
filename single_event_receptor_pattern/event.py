from enum import Enum, auto

class EventType(Enum):
    BATTERY_LOW = auto()
    BATTERY_NORMAL = auto()
    BATTERY_CRITICAL = auto()


class SystemState(Enum):
    NORMAL = auto()
    LOW_POWER = auto()
    CRITICAL_SAVING = auto()


class Event:
    def __init__(self, event_type, data=None):
        self.event_type = event_type
        self.data = data