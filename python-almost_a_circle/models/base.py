#!/usr/bin/python3
"""Base class module."""

import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Turn data from python to JSON."""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return JSON string representation."""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation to a file."""
        filename = f"{cls.__name__}.json"
        dict_rep = []

        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                dict_rep.append(list_objs[i].to_dictionary())

        list_rep = cls.to_json_string(dict_rep)

        with open(filename, 'w') as file:
            file.write(list_rep)

    @classmethod
    def create(cls, **dictionary):
        """Return instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = f"{cls.__name__}.json"

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as file:
            content = file.read()

        list_of_class = cls.from_json_string(content)
        list_of_instances = []

        for i in range(len(list_of_class)):
            list_of_instances.append(cls.create(**list_of_class[i]))

        return list_of_instances
