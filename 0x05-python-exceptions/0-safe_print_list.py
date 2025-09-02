#!/usr/bin/python3

"""
    Function to print certainn nuber of element from
    a given list
"""


def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print(my_list[i], end='')
        except IndexError:
            break
        i += 1
    print()
    return i
