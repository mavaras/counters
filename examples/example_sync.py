from counters.counters import counter
from counters.utils import format_calls, format_levels


@counter
def first():
    third()
    second()


@counter
def second():
    pass


@counter
def third():
    fourth()
    second()


@counter
def fourth():
    second()


@counter
def main():
    for _ in range(1):
        first()

main()
format_levels()
format_calls()
