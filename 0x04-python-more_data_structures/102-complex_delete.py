#!/usr/bin/python3

"""
    Module to perform complex deletion
    operation on a given dictionary using the value given
"""


def complex_delete(a_dictionary, value):
    keys = list(a_dictionary)
    for key in keys:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary

