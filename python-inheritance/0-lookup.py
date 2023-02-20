#!/usr/bin/python3
"""Function to return a list of an object's content."""


def lookup(obj):
    """Return attributes and methods of an object.

    Args:
        obj: object given
    """
    return list(dir(obj))
