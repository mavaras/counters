# Single unittesting file

from counters.utils import (
    is_async, update_levels, update_stats
)
from counters.cvars import LEVELS, STATS


def test_update_levels():
    mock_element = {'fname': 'test', 'level': 1}
    update_levels(mock_element)
    assert len(LEVELS.get()) == 1 and LEVELS.get()[0] == mock_element
    mock_element = {'fname': 'test2', 'level': 1}
    update_levels(mock_element)
    assert len(LEVELS.get()) == 2 and LEVELS.get()[-1] == mock_element
    mock_element = {'fname': 'test', 'level': 1}
    update_levels(mock_element)
    assert len(LEVELS.get()) == 3 and LEVELS.get()[-1] == mock_element
    mock_element = {'fname': 'test', 'level': 1}
    update_levels(mock_element)
    assert len(LEVELS.get()) == 3 and LEVELS.get()[-1] == mock_element


def test_update_stats():
    mock_element = {'fname': 'test', 'calls': 1}
    update_stats(mock_element['fname'])
    assert len(STATS.get()) == 1 and STATS.get()[0] == mock_element
    mock_element = {'fname': 'test', 'calls': 2}
    update_stats(mock_element['fname'])
    assert len(STATS.get()) == 1 and STATS.get()[0] == mock_element
    mock_element = {'fname': 'test2', 'calls': 1}
    update_stats(mock_element['fname'])
    assert len(STATS.get()) == 2 and STATS.get()[-1] == mock_element

def test_is_async():
    async def mock_function():
        pass
    assert is_async(mock_function)
