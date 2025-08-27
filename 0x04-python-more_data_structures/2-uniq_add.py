#!/usr/bin/python3

"""
    Function to add only unique
    integers in a given list
"""


def uniq_add(my_list=[]):
    res = 0
    for i in range(len(my_list)):
        res = res + my_list[i]
        for x in range(i):
            if my_list[x] == my_list[i]:
                res = res - my_list[i]
            else:
                continue
    return res
