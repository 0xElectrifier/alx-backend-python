#!/usr/bin/env python3
"""Defines a type-annotated function `safe_first_element`"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of list @lst, or None if lst is None"""
    if lst:
        return lst[0]
    else:
        return None
