#!/usr/bin/python3

"""
    Function to print element of a list
    in reverse.
"""


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
