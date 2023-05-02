#!/usr/bin/python3
"""Defines a type-annotated function `to_str`"""


def to_str(n: float) -> str:
    """Returns the string representation of @n"""
    return n.__str__()
