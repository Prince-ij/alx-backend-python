#!/usr/bin/env python3
"""
measures time it takes to execute async_comprehension
"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the time taken to call async_comprehension
    """

    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    time = end - start
    return time
