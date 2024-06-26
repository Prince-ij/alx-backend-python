#!/usr/bin/env python3
"""
Use async generator to loop
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    asynchronously loops ten times and generates
    random numbers from 0 to ten
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
