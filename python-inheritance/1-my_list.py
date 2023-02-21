#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        new = list.copy(self)
        print(sorted(new))
