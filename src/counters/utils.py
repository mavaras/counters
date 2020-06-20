import inspect
from typing import (
    Callable, Dict, Union
)
from contextlib import contextmanager
from contextvars import ContextVar
from cvars import CHAR_CHECK_MARK, INDENT_SEQ, LEVELS, STATS


@contextmanager
def increase_counter(contextvar: ContextVar):
    token = contextvar.set(contextvar.get() + 1)
    try:
        yield
    finally:
        contextvar.reset(token)


def levels():
    format_levels()


def format_levels():
    print(f'\n{CHAR_CHECK_MARK} Traced functions nested call chain\n')
    print(f'{INDENT_SEQ}L{INDENT_SEQ}', end='')
    for i in range(1, len(LEVELS) - 1):
        print(f'{i}{INDENT_SEQ}', end='')
    print()
    for level in LEVELS:
        fname = level['fname']
        indent = f'|{INDENT_SEQ}' * level['level']
        print(f'{INDENT_SEQ}{indent}·-> {fname}')
    print()


def format_calls(ascendant: boolean = True):
    print(f'\n{CHAR_CHECK_MARK} Traced functions and its number of calls\n')
    for stat in STATS[::-ascendant]:
        fname = stat['fname']
        calls = stat['calls']
        print(f'{INDENT_SEQ}{fname} ·-> {calls}')
    print()


def is_async(function: Callable) -> bool:
    return inspect.iscoroutinefunction(function)


def update_levels(new_element: Dict[str, Union[str, int]]):
    last_element = LEVELS[-1] if LEVELS else []
    if new_element != last_element:
        LEVELS.append(new_element)


def update_stats(key: str):
    fnames = [list(e.values())[0] for e in STATS]
    if key in fnames:
        STATS[fnames.index(key)]['calls'] += 1
    else:
        STATS.append({'fname': key, 'calls': 1})
