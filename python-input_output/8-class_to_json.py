#!/usr/bin/python3
"""Return a dictionary description for JSON serialization."""


def class_to_json(obj):
    """Return dictionary."""
    return obj.__dict__
