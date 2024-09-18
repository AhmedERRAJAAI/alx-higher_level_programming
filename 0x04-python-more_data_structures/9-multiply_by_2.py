#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dict = {}
    for dc in a_dictionary:
        b_dict[dc] = a_dictionary[dc]*2
    return b_dict
