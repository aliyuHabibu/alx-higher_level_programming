#!/usr/bin/python3

"""
    Function to find the largest int element
    in a given list of integer.
"""


def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None
    n = 0
    for i in range(len(my_list)):
        for x in range(len(my_list)):
            if ((my_list[i] > my_list[x]) and (x == len(my_list) -1)):
                return my_list[i]
