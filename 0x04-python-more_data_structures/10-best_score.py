#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        scores_values_len = len(a_dictionary.values())
        if scores_values_len > 0:
            score = max(a_dictionary.values())
            for key in a_dictionary.keys():
                if a_dictionary[key] == score:
                    return key
    return None
