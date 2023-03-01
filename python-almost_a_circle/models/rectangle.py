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
        return self.width

    @width.setter
    def width(self, value):
        self.width = value

    @property
    def height(self):
        """Getter method."""
        return self.height

    @height.setter
    def height(self, value):
        self.height = value

    @property
    def x(self):
        """Getter method."""
        return self.x

    @x.setter
    def x(self, value):
        self.x = value

    @property
    def y(self):
        """Getter method."""
        return self.y

    @y.setter
    def y(self, value):
        self.y = value
