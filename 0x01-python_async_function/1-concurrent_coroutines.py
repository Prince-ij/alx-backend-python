#!/usr/bin/env python3
"""
A module that spawns wait_random n times using
a coroutine wait_n
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n number of times

    Args:
    n (int) : number of times to spawn
    max_delay (int) : max interval in random.uniform
    Returns:
    List[float] : a list of floats in acending order
    """

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
