#!/usr/bin/python3

"""
    Function to remove a character
    in a given set of string
"""


def no_c(my_string):
    my_string = list(my_string)
    for i in my_string:
        if i == 'C' or i == 'c':
            my_string.remove(i)
    return ''.join(my_string)
