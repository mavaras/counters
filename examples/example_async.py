import asyncio
from counters.counters import counter
from counters.utils import format_calls, format_levels


@counter
async def first():
    await third()
    await second()


@counter
async def second():
    pass


@counter
async def third():
    await fourth()
    await second()


@counter
async def fourth():
    await second()


@counter
async def main():
    for _ in range(1):
        asyncio.create_task(first())

asyncio.run(main())
format_levels()
format_calls()
