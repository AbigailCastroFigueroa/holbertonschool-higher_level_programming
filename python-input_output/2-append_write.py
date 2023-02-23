#!/usr/bin/python3
#!/usr/bin/python3
"""Appending text to file method."""


def append_write(filename="", text=""):
    """Add new text at the end to the given file."""
    with open(filename, 'a') as file:
        count = file.write(text)
        return count
    with open(filename, 'r', 'utf-8') as file:
        for line in file:
            print(line.split())
