#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(len(my_list)):
        if i < x:
            print("{}".format(my_list[i]), end="")
            count += 1
    print()
    return count
