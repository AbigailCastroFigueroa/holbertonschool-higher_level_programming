#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size < 0 and size is float:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for i in range(size):
                print("#", end="")
            print()
