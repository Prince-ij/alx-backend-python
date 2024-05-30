#!/usr/bin/env python3
"""
Create multiple tasks with asyncio.create_tasks
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create several tasks using wait_random

    Args:
    n (int): max delay (int): self explanatory

    Returns:
    list of floats
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
