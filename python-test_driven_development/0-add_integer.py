#!/usr/bin/python3
"""Addition Module."""


def add_integer(a, b=98):
    """Addition method of two values.

    Args:
        a: first value.
        b: second value.
    """
    try:
        return int(a + b)
    except TypeError:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        elif not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
