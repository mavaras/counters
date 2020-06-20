import inspect
from typing import Any, Callable, List, Union
from cvars import LEVELS
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
    for level in LEVELS:
        fname = level['fname']
        indent = '|     ' * level['level']
        print(f'{indent}·-> {fname}')


def is_async(function: Callable) -> bool:
    return inspect.iscoroutinefunction(function)


def update_dict_array(
    keys: List[str],
    values: List[Union[str, int]],
    array: List[Any],
    unique_values: bool = True,
):
    new_element = {keys[i]: values[i] for i in range(len(keys))}
    if new_element not in array:
        array.append(new_element)
