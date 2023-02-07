#!/usr/bin/python3
"""Square class module."""


class Square:
    """Square class method."""

    def __init__(self, size=0):
        """Documentation of __init__ method.

        Args:
            size: size of a square.
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Documentation of area method.

        Args:
            self: return the area of the square
        """
        return self.__size * self.__size
