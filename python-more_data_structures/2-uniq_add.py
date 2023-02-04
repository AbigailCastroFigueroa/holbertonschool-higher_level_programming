#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = sorted(set(my_list))
    return sum(new[:])
