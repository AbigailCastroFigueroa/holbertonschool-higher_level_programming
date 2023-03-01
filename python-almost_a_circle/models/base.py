#!/usr/bin/python3
"""Base class module."""


class Base:
    """Base class as constructor."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Return id value."""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
