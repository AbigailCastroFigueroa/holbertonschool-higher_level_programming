#!/usr/bin/python3
"""Square class module."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherit from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor method."""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a custom string."""
        a = str(self.id)
        b = str(self.x)
        c = str(self.y)
        d = str(self.width)
        return "[Square] (" + a + ") " + b + "/" + c + " - " + d

    @property
    def size(self):
        """Getter method."""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """Assings arguments to each attribute."""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """Return dictionary representation."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
