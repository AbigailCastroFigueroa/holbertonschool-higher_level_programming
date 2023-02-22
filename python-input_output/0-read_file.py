#!/usr/bin/python3
"""Reading file method."""


def read_file(filename=""):
    """Read a file given."""
    if filename == "":
        return ""
    with open(filename, encoding='utf-8') as file:
        print(file.read())
