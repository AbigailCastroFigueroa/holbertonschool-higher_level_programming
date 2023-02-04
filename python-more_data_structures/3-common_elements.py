#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = []
    for i in set_1:
        for j in set_2:
            if i == j:
                new.append(j)
    return new
