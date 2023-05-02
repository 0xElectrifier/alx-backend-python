#!/usr/bin/env python3
"""Defines a type-annotated function `to_kv`"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple which contains a string and/or float"""
    return (k, v);
