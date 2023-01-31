#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    if my_list != 0:
        length = len(my_list)
        while length > 0:
            print("{:d}".format(my_list[length - 1]))
            length -= 1
