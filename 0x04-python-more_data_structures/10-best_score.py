#!usr/bin/python3
def best_score(a_dictionary):
    greatest_key=None
    ref = 0
    for key in a_dictionary:
        if a_dictionary[key] > ref:
            greatest_key = key
