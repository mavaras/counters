from functools import wraps

from counters.cvars import (
    FLOW, LEVEL
)
from counters.utils import (
    increase_counter, is_async, noop,
    update_levels, update_stats
)


def counter(function=None, block=False):
    def decorator(function):
        fname = function.__name__
        if is_async(function):
            fname = f'async {fname}'
            @wraps(function)
            async def wrapper(*args, **kwargs):
                wrapper.calls += 1
                if block and wrapper.calls > block:
                    return noop
                with increase_counter(LEVEL):
                    FLOW.append(function.__name__)
                    update_stats(fname)
                    update_levels({'fname': fname, 'level': LEVEL.get()})
                    await function(*args, **kwargs)
        else:
            @wraps(function)
            def wrapper(*args, **kwargs):
                wrapper.calls += 1
                if block and wrapper.calls > block:
                    return noop
                with increase_counter(LEVEL):
                    FLOW.append(function.__name__)
                    update_stats(fname)
                    update_levels({'fname': fname, 'level': LEVEL.get()})
                    function(*args, **kwargs)

        wrapper.calls = 0
        return wrapper
    return decorator if not function else decorator(function)
