#!/usr/bin/python3

"""
    Function that replace the element of
    a list at a given index with another value
"""


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    else:
        my_list.pop(idx)
        my_list.insert(idx, element)
        return my_list
