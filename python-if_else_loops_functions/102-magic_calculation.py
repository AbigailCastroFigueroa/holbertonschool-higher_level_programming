#!/usr/bin/python3
def magic_calculation(a, b, c):
    if not (b < a):
        return c
    elif not (b > c):
        return a + b
    else:
        return (a*b)-c