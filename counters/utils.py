import inspect
from typing import (
    Callable, Dict, Generator, List, Optional, Union
)
from contextlib import contextmanager
from contextvars import ContextVar
from counters.cvars import (
    CHAR_CHECK_MARK, INDENT_SEQ, LEVELS, STATS
)


@contextmanager
def increase_counter(contextvar: ContextVar) -> Generator:
    token = contextvar.set(contextvar.get() + 1)
    try:
        yield
    finally:
        contextvar.reset(token)


def format_levels():
    print(f'\n{CHAR_CHECK_MARK} Traced functions nested call chain\n')
    print(f'{INDENT_SEQ}L{INDENT_SEQ}', end='')
    for i in range(1, len(STATS.get()) + 4):
        print(f'{i}{INDENT_SEQ}', end='')
    print()
    for level in LEVELS.get():
        fname = level['fname']
        indent = f'|{INDENT_SEQ}' * level['level']
        print(f'{INDENT_SEQ}{indent}·-> {fname}')
    print()


def format_calls(ascendant: bool = True):
    print(f'\n{CHAR_CHECK_MARK} Traced functions with its number of calls\n')
    for stat in STATS.get()[::-ascendant]:
        fname = str(stat['fname'])
        calls = int(stat['calls'])
        print(f'{INDENT_SEQ}{fname} ·-> {calls}')
    print()


def is_async(function: Callable) -> bool:
    return inspect.iscoroutinefunction(function)


def update_levels(new_element: Dict[str, Union[str, int]]):
    last_element: Optional[Dict[str, Union[str, int]]] = \
        LEVELS.get()[-1] if LEVELS.get() else None
    if new_element != last_element:
        aux = LEVELS.get()
        aux.append(new_element)
        LEVELS.set(aux)


def update_stats(key: str):
    fnames = [list(e.values())[0] for e in STATS.get()]
    if key in fnames:
        indx = fnames.index(key)
        aux = STATS.get()
        aux[indx]['calls'] += 1  # type: ignore
        STATS.set(aux)
    else:
        aux = STATS.get()
        aux.append({'fname': key, 'calls': 1})
        STATS.set(aux)


def noop():
    pass
