#!/usr/bin/python3
"""Conversion from obj to JSON."""

import json


def to_json_string(my_obj):
    """Convert a python object to a string."""
    return json.dumps(my_obj)
