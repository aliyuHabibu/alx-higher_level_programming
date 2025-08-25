#!/usr/bin/python3

"""
    Function to take two tuples and add
    them together base on there individual
    index of element
"""


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    if len(tuple_a) == 0:
        return tuple(tuple_b)
    elif len(tuple_b) == 0:
        return tuple(tuple_a)
    else:
        if len(tuple_a) == 2 and len(tuple_b) == 1:
            new_tuple.append(tuple_a[0] + tuple_b[0])
            new_tuple.append(tuple_a[1])
            return tuple(new_tuple)
        elif len(tuple_a) == 1 and len(tuple_b) == 2:
            new_tuple.append(tuple_a[0] + tuple_b[0])
            new_tuple.append(tuple_b[1])
            return tuple(new_tuple)
        else:
            new_tuple.append(tuple_a[0] + tuple_b[0])
            new_tuple.append(tuple_a[1] + tuple_b[1])
            return tuple(new_tuple)
