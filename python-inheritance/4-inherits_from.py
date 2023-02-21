#!/usr/bin/python3
"""Module for the inherits_from method."""


def inherits_from(obj, a_class):
    """Return boolean expresion."""
    a = type(obj)
    if issubclass(a, a_class) and a is not a_class:
        return True
    return False
