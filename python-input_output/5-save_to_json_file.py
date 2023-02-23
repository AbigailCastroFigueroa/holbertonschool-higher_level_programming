#!/usr/bin/python3
"""Writes an object to a JSON text file."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file."""
    with open(filename, 'w') as file:
        count = json.dump(my_obj, file)
        return count
    with open(filename, 'r', 'utf-8') as file:
        for line in file:
            print(line.split())
