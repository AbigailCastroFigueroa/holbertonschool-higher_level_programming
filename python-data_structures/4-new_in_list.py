#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    new_list = list.copy(my_list)
    if 0 > idx or idx > length:
        return (new_list)
    new_list[idx] = element
    return (new_list)
