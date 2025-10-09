#!/usr/bin/python3

"""
    Function to remove a character
    in a given set of string
"""


def no_c(my_string):
    string = list(my_string)
    i = 0
    while i < len(string):
        if string[i] == 'C':
            string.remove(string[i])
            i = i - 1
        if string[i] == 'c':
            string.remove(string[i])
            i = i - 1
        i = i + 1
    return ''.join(string)
