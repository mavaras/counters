from contextvars import ContextVar
from typing import List, NamedTuple


Fcall = NamedTuple('Fcall', [
    ('fname', str),
    ('level', int),
    ('calls', int),
])

LEVEL: ContextVar[int] = ContextVar('LEVEL', default=0)
STATS: List[Fcall] = []
LEVELS: List[Fcall] = []

FLOW: List[str] = []
