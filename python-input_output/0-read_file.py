#!/usr/bin/python3
"""Reading file method."""


def read_file(filename=""):
    """Read a file given."""
    with open(filename, 'r') as file:
        print(file.read())
