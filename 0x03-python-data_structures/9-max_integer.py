#!/usr/bin/python3

"""
    Function to find the largest int element
    in a given list of integer.
"""


def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None
    large = my_list[0]
    for num in my_list:
        if (num > large):
            large = num
    return large
