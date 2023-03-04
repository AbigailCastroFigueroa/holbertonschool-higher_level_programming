#!/usr/bin/python3
"""Rectangle class module."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class methods."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """Getter method."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print a representation of the rectangle."""
        for i in range(self.__y):
            print()
        for row in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width, end="")
            print()

    def __str__(self):
        """Return a custom string."""
        a = str(self.id)
        b = str(self.width)
        c = str(self.__height)
        d = str(self.__x)
        e = str(self.__y)
        return "[Rectangle] (" + a + ") " + d + "/" + e + " - " + b + "/" + c

    def update(self, *args, **kwargs):
        """Assings arguments to each attribute."""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.id = args[0]
                    self.__width = args[1]
                elif i == 2:
                    self.id = args[0]
                    self.__width = args[1]
                    self.__height = args[2]
                elif i == 3:
                    self.id = args[0]
                    self.__width = args[1]
                    self.__height = args[2]
                    self.__x = args[3]
                elif i == 4:
                    self.id = args[0]
                    self.__width = args[1]
                    self.__height = args[2]
                    self.__x = args[3]
                    self.__y = args[4]
                else:
                    self
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
