from contextvars import ContextVar
from typing import Dict, List, Union


LEVEL: ContextVar[int] = ContextVar('LEVEL', default=0)
STATS: ContextVar[List[Dict[str, Union[str, int]]]] = \
    ContextVar('STATS', default=[])
LEVELS: ContextVar[List[Dict[str, Union[str, int]]]] = \
    ContextVar('LEVELS', default=[])

FLOW: List[str] = []

CHAR_CHECK_MARK: str = chr(0X2713)
INDENT_SEQ: str = '    '
