#!/usr/bin/python3
"""Say my name module."""


def say_my_name(first_name, last_name=""):
    """Documentation of the say_my_name method.

    Args:
        first_name: First name of the person
        last_name: Last name of the person
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("{} {}".format(first_name, last_name))
