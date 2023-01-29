#!/usr/bin/python3
def element_at(my_list, idx):
    if 0 < idx > len(my_list) - 1:
        return None
    elif idx == 0:
        return my_list[0]
    for i in my_list:
        if i == idx:
            return my_list[i]
