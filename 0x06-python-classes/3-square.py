#!/usr/bin/python3

"""
    Module that defines the class sqaure
"""


class Square:
    """
        square:
            Implemnetation of class square
            """
    def __init__(self, size=0):
        """ Initialization method """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Method that compute and return the area of a square """
        return self.__size * self.__size
