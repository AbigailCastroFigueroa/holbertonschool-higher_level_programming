#!/usr/bin/python3
"""Convert a string from json to object."""

import json


def from_json_string(my_str):
    """Convert a given json string to obj."""
    return json.loads(my_str)
