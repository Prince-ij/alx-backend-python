#!/usr/bin/env python3
"""
Use async generator comprehension
"""

import random
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    using async comprehension to call async_generator
    """

    return [number async for number in async_generator()]
