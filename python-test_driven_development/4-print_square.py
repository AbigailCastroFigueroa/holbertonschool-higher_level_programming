#!/usr/bin/python3
"""Print_Square module."""


def print_square(size):
    """print square method.

    Args:
        size: size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size < 0 and size is float:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for i in range(size):
                print("#", end="")
            print()
