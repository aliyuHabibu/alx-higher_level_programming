#!/usr/bin/python3

"""
    Script to import a function and perform
    an operations with it.
"""

from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    my_sum = add(a, b)
    print("{} + {} = {}".format(a, b, my_sum))
