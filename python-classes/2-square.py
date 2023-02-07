#!/usr/bin/python3
"""Square Class module."""


class Square:
    """Square class method."""

    def __init__(self, size=0):
        """Documentation of __init__method.

        Args:
            size: size of the square.
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
