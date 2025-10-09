#!/usr/bin/python3

"""
    Module to get the weighted average of
    set of number given
"""


def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    ml, sm = 0, 0
    for sett in my_list:
        ml += sett[0] * sett[1]
        sm += sett[1]
    return ml / sm
