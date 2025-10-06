#!/usr/bin/python3

"""
    Function to modify a given list at an index
    without modifying the original list
"""


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0:
        return new_list
    elif idx > len(my_list) - 1:
        return new_list
    else:
        new_list.pop(idx)
        new_list.insert(idx, element)
        return new_list
