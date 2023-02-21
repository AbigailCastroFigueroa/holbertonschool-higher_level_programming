#!/usr/bin/python3
"""Module for the is_kind_of_class method."""


def is_kind_of_class(obj, a_class):
    """Return a boolean expression."""
    if isinstance(obj, a_class) == True:
        return True
    return False
