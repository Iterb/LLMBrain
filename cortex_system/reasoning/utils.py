from enum import Enum, auto


class ReasoningLevel(Enum):
    TOP_LEVEL = auto()
    MID_LEVEL = auto()
    FINE_GRAINED = auto()
    HEALTH_CHECK = auto()
