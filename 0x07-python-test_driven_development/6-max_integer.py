#!/usr/bin/python3
"""Module to find the max integer in a list
"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the funtion returns None
    """
    if len(list) == 0:
        return None

    for i in range(len(list)):
        if not type(list[i]) == int:
            raise TypeError("An element is not an int")

    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
