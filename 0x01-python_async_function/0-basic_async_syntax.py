#!/usr/bin/env python3
"""
Using asyncio in practice
"""

import asyncio
import random


async def wait_random(max_delay: int) -> float:
    """
    delays uniformly from 0 to max delay
    and returns random float

    Args:
    max_delay (int): maximum delay interval

    Returns:
    float : the delay in seconds
    """

    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
