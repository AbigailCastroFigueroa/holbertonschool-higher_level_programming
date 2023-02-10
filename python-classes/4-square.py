#!/usr/bin/python3
"""Square class module."""


class Square:
    """Square class methods."""

    def __init__(self, size=0):
        """Documentation of __init__ method.

        Args:
            size: size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Getter method."""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Documentation of area method.

        Args:
            self: return the area of the square.
        """
        return self.__size * self.__size
