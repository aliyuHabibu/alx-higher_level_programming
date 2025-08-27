#!/usr/bin/python3

"""
    Function to multiply all values of a
    dictionary with a specified given value
"""


def multiply_by_2(a_dictionary):
    ret_dict = {}
    sorted_dict = sorted(a_dictionary)
    for i in range(len(a_dictionary)):
        ret_dict[sorted_dict[i]] = a_dictionary[sorted_dict[i]] * 2
    return ret_dict
