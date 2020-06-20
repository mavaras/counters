from functools import wraps
import inspect
import asyncio
from typing import Any, Callable, List, Union
from tracers.function import trace

from cvars import (
    FLOW, LEVEL, LEVELS, STATS
)
from utils import (
    format_levels, format_calls,
    increase_counter, is_async, update_dict_array
)


def get_stats():
    return STATS


def get_levels():
    return LEVELS


def counter(function):
    fname = function.__name__
    if is_async(function):
        fname = f'async {fname}'
        @wraps(function)
        async def wrapper(*args, **kwargs):
            wrapper.calls += 1
            with increase_counter(LEVEL):
                FLOW.append(function.__name__)
                update_dict_array(['fname', 'calls'], [fname, wrapper.calls], STATS)
                update_dict_array(['fname', 'level'], [fname, LEVEL.get()], LEVELS)
                await function(*args, **kwargs)
    else:
        @wraps(function)
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            with increase_counter(LEVEL):
                FLOW.append(function.__name__)
                update_dict_array(['fname', 'calls'], [fname, wrapper.calls], STATS)
                update_dict_array(['fname', 'level'], [fname, LEVEL.get()], LEVELS)
                function(*args, **kwargs)

    wrapper.calls = 0
    return wrapper
