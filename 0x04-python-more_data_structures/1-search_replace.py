#!/usr/bin/python3

"""
    Function to search for an element
    in a list and replace it with a given value
"""


def search_replace(my_list, search, replace):
    cp_list = my_list.copy()
    ret_list = []
    for i in range(len(cp_list)):
        if cp_list[i] == search:
            ret_list.append(replace)
        else:
            ret_list.append(cp_list[i])
    return ret_list
