#!/usr/bin/env python3
"""
Create a task using create_task method of asyncio
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create a task from wait random

    Args:
    max_delay (int): max interval range for wait_random

    Returns:
    asyncio.Task: an async task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
