#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = list.copy(my_list)
    for i in new:
        if i % 2 != 0:
            new[i] = False
        else:
            new[i] = True
    i += 1
    return new
