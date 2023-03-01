#!/usr/bin/python3
"""Rectangle class module."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class methods."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor."""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = super().__init__(id)

    @property
    def width(self):
        """Getter method."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Getter method."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Getter method."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Getter method."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
