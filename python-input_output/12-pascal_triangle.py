#!/usr/bin/python3
"""Pascal square function."""


def pascal_triangle(n):
    """Pascal square function."""
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        var = str(11 ** i)
        triangle.append(var)
    return triangle
