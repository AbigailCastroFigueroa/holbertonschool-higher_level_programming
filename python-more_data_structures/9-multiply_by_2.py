#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for item in a_dictionary.keys():
        new[item] *= 2
    return new
