#!/usr/bin/env python3
"""Defines a type-annotation function `sum_mixed_list`"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of all items in @mxd_list"""
    sum: float = 0
    for item in mxd_list:
        sum += item

    return sum
