#!/usr/bin/env python3
"""Defines a type-annotated function `make_multiplier`"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by @multiplier"""
    def mul_callback(numb: float) -> float:
        """Callback function that multiplies @numb by @multiplier"""
        return multiplier * numb
    return mul_callback
