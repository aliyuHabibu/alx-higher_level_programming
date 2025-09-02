#!/usr/bin/python3

"""
    Function to safely print only
    integer value given to the function
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
