#!/usr/bin/python3

"""
    Function to get an element at
    an index given.
"""


def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list) - 1:
        return None
    else:
        return my_list.pop(idx)
