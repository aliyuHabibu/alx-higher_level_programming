#!/usr/bin/python3

"""
    Module that defines the class square
"""


class Square:
    """
        square:
            Implementation of the class square
            """
    def __init__(self, size=0):
        """ initialization method """
        self.size = size

    @property
    def size(self):
        """ size getter method """
        return self.__size

    @size.setter
    def size(self, value):
        """ size settter method """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ method that compute and return the area of a square """
        return self.__size * self.__size
