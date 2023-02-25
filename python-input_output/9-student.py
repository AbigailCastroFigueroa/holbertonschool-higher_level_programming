#!/usr/bin/python3
"""Student class module."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Student class methods."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary."""

        return self.__dict__
