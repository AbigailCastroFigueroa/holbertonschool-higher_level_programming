#!/usr/bin/python3
"""Student class module."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Student class methods."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary."""
        dict_to_return = dict()
        if type(attrs) is list and all(type(i) is str for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    dict_to_return.update({i: self.__dict__[i]})
            return dict_to_return
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attribute values of a class instance."""
        for i, j in json.items():
            self.__dict__[i] = j
