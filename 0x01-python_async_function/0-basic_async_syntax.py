#!/usr/bin/env python3
"""Defines function for Task 0 module"""


async def wait_random(max_delay: int = 10) -> float:
    """Async function that waits for random delay"""
    import asyncio
    import random
    i = random.uniform(0.0, max_delay)
    await asyncio.sleep(i)

    return i
