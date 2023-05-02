#!/usr/bin/env python3
"""Defines a type-annotated function `sum_list`"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of all items in @input_list"""
    sum: float = 0
    for item in input_list:
        sum += item

    return sum
