#!/usr/bin/env python3
"""
Measures runtime for wait_n
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures runtime for wait_n function

    Args:
    n (int): number of time to spawn wait_random
    max_delay (int): max interval for wait_random

    Returns:
    float: seconds taken to execute wait_n
    """

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total = end - start
    return total / n
