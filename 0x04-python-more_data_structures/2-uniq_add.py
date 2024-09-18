#!/usr/bin/python3

def uniq_add(my_list=[]):
    passed = []
    for x in my_list:
        if x in passed:
            continue
        passed.append(x)

    return sum(passed)
