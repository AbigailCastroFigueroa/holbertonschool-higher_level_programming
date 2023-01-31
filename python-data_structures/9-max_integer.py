#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0 or my_list == []:
        return None
    elif my_list is None:
        return None
    else:
        new = sorted(list.copy(my_list))
        return new[-1]
