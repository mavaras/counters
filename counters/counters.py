from functools import wraps

from counters.cvars import (
    FLOW, LEVEL, LEVELS, STATS
)
from counters.utils import (
    increase_counter, is_async,
    update_levels, update_stats
)


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
