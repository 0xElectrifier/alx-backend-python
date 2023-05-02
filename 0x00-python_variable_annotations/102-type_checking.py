#!/usr/bin/env python3
"""Defines a type-annotated function for Task 12."""
from typing import List, Tuple, Union


def zoom_array(lst: Union[List, Tuple], factor: Union[float, int] = 2) -> List:
    """Creates multiple copies of items in a tuple, @lst."""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3.0)
