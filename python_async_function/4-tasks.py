#!/usr/bin/env python3
"""Module for task_wait_n using task_wait_random."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times concurrently and return delays in order.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay passed to each task_wait_random call.

    Returns:
        List[float]: Delays in ascending order (no sort() used).
    """
    delays: List[float] = []
    for task in asyncio.as_completed([task_wait_random(max_delay) for _ in range(n)]):
        delay = await task
        delays.append(delay)
    return delays
