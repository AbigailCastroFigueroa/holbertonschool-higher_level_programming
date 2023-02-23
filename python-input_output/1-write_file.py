#!/usr/bin/python3
"""Writing file method."""


def write_file(filename="", text=""):
    """Write a given text to a given file."""
    with open(filename, 'w') as file:
        count = file.write(text)
        return count
    with open(filename, 'r', 'utf-8') as file:
        for line in file:
            print(line.split())
