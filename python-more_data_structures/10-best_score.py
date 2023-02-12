#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    elif not bool(a_dictionary):
        return None
    else:
        i = list(a_dictionary.values())
        j = list(a_dictionary.keys())
    return (j[i.index(max(i))])
