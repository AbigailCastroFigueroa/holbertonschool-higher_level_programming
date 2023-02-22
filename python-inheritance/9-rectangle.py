#!/usr/bin/python3
"""Rectangle class Module."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class methods."""

    def __init__(self, width, height):
        """Rectangle class method."""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """Return the area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Print a string."""
        a, b = str(self.__width), str(self.__height)
        return '[Rectangle] ' + a + '/' + b
