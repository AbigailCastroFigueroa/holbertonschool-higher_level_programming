#!/usr/bin/python3
"""BaseGeometry class module."""


class BaseGeometry:
    """BaseGeometry class methods."""

    def area(self):
        """Veryfies the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Veryfies tha value if an integer."""
        if type(value) is not int:
            raise TypeError('' + str(name) + ' must be an integer')
        if value <= 0:
            raise ValueError('' + str(name) + ' must be greater than 0')
