#!/usr/bin/python3
"""Function that adds 2 integers"""


def add_integer(a, b=98):
    """Add integers a and b with conditions:
    - Must be integers or floats
    - Must be first casted to integers if they are float"""
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
