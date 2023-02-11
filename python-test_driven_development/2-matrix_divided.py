#!/usr/bin/python3
"""Division method module."""


def matrix_divided(matrix, div):
    """Division of a matrix.

    Args:
        matrix: given matrix.
        div: given divisor.
    """
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, (int, float, list)):
        raise TypeError(
            "matrix must be a matrix (list of list) of integers/float")
    for row in matrix:
        for var in row:
            if not isinstance(var, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of list) of integers/float")
    return [[round((var / div), 2) for var in row] for row in matrix]
