#!/usr/bin/env python3
"""Defines an async function for Task 1 module"""

wait_random = __import__("0-basic_async_syntax").wait_random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls `wait_random` function @n time with max_delay
    Args:
        n (int): The number of times to call `wait_random` function
        max_delay (int): The maximum limit of delay in seconds
    Returns: A list of all delays
    """
    delays: List[float] = []
    for i in range(n):
        delays.append(await wait_random(max_delay))

    return delays
