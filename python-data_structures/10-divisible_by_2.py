#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = list.copy(my_list)
    for i in range(len(my_list)):
        if new[i] % 2 != 0:
            new[i] = False
        else:
            new[i] = True
    return new
