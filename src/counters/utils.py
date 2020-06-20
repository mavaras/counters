import inspect
from typing import Any, Callable, List, Union
from cvars import CHAR_CHECK_MARK, INDENT_SEQ, LEVELS, STATS
from contextlib import contextmanager


@contextmanager
def increase_counter(contextvar):
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


def format_calls(ascendant=True):
    print(f'\{CHAR_CHECK_MARK} Traced functions and its number of calls\n')
    for stat in STATS[::-ascendant]:
        fname = stat['fname']
        calls = stat['calls']
        print(f'{INDENT_SEQ}{fname} ·-> {calls}')
    print()


def is_async(function: Callable) -> bool:
    return inspect.iscoroutinefunction(function)


def update_dict_array(
    keys: List[str],
    values: List[Union[str, int]],
    array: List[Any],
    unique_values: bool = True,
):
    new_element = {keys[i]: values[i] for i in range(len(keys))}
    last_element = array[-1] if array else []
    if new_element != last_element:
        array.append(new_element)
