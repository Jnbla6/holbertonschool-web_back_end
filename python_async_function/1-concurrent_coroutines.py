#!/usr/bin/env python3
"""Module for concurrent coroutines - wait_n routine."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times concurrently and return delays in order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay passed to each wait_random call.

    Returns:
        List[float]: Delays in ascending order (no sort() used).
    """
    delays: List[float] = []
    for coro in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        delay = await coro
        delays.append(delay)
    return delays
