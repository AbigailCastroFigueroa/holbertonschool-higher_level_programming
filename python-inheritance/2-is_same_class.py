#!/usr/bin/python3
"""Module for the is_same_class method."""


def is_same_class(obj, a_class):
    """Return boolean expression."""
    if type(obj) is a_class:
        return True
    return False
