#!/usr/bin/python3

"""
    Function to take each ekement of a list
    a mutiply it with a given value using map function
"""


def multiply_list_map(my_list=[], number=0):
    mp = map(lambda x: x * number, my_list)
    return list(mp)
