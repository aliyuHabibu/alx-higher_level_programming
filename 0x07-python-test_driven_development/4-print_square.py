#!/usr/bin/python3

"""
    Module to print a character in
        a square shape
"""


def print_square(size):
    """
        This is the function which print the square
            args:
                size - The size of square to print.
            if the type of size is not an int
                or it is equal to zero
                then raise an error
                """
    if not type(size) == int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        x = 0
        while x < size:
            print("#", end='')
            x += 1
        print()
