#!/usr/bin/python3
"""Rectangle Class Module."""


class Rectangle:
    """Creates a class called Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle.

        Args:
            self: reference to the object itself.
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """Getter Method."""
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")

        @property
        def height(self):
            """Getter Method."""
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
