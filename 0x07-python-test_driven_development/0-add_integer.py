#!/usr/bin/python3

"""
    This is the Addition Module.
    Takes two args and compute.
    And return the sum.
"""


def add_integer(a, b=98):
    """   Addition Function.
            args: a, b.
    """
    if a is None:
        raise TypeError("a must be an integer")
    elif b is None:
        raise TypeError("b must be an integer")
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif type(a) and type(b) not in [int, float]:
        raise TypeError("a and b must be an integer")
    else:
        return int(a + b)
