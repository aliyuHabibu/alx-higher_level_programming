#!/usr/bin/python3

"""
    Function to return the key
    with the largest value
"""


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        vals = list(a_dictionary.values())
        larVal = vals[0]
        for keys in a_dictionary:
            if a_dictionary[keys] > larVal:
                larVal = a_dictionary[keys]
                key = keys
        return key
