#!/usr/bin/python3

"""
    Function to safely print only integers of a
    given list with a combination of other element
    in the list
"""


def safe_print_list_integers(my_list=[], x=0):
    i, n = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            n += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return n
