#!/usr/bin/python3
"""MyInt class module."""


class MyInt(int):
    """MyInt class method."""

    def check_instance(self, int):
        """Return inverted boolean expression."""
        if isinstance(int, int):
            return False
        return True
