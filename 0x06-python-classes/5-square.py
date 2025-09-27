#!/usr/bin/python3

"""
    Module implementing the class square
"""


class Square:
    """
        suare:
            Implementation of the class square
            """
    def __init__(self, size=0):
        """ Initialization of class instances  """
        self.size = size

    @property
    def size(self):
        """ Getter method for instamce attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for the size instance attribute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ method that compute and return the area of a square """
        return self.__size * self.__size

    def my_print(self):
        """ Method to print a square form using # """
        if self.__size == 0:
            print()
        else:
            r = 0
            while r < self.__size:
                i = 0
                while i < self.__size:
                    print("#", end='')
                    i += 1
                print()
                r += 1
