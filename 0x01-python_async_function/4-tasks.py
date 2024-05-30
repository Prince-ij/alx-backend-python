#!/usr/bin/env python3
"""
Create multiple tasks with asyncio.create_tasks
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create several tasks using wait_random

    Args:
    n (int): max delay (int): self explanatory

    Returns:
    asyncio.Task
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = asyncio.gather(*tasks)
    return sorted(results)