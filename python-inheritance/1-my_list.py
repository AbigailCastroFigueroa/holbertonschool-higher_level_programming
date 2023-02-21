#!/usr/bin/python3
"""Class inherit from list class."""


class MyList(list):
    """class MyList."""

    def print_sorted(self):
        """Print a sorted list."""
        new = list.copy(self)
        print(sorted(new))
