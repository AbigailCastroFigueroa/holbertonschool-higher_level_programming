#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for var in row:
            print("{} ".format(var), end="")
        print()
