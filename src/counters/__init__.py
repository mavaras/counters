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
    increase_counter, is_async,
    update_levels, update_stats
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
                update_stats(fname)
                update_levels({'fname': fname, 'level': LEVEL.get()})
                await function(*args, **kwargs)
    else:
        @wraps(function)
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            with increase_counter(LEVEL):
                FLOW.append(function.__name__)
                update_stats(fname)
                update_levels({'fname': fname, 'level': LEVEL.get()})
                function(*args, **kwargs)

    wrapper.calls = 0
    return wrapper
