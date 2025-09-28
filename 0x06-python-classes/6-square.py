#!/usr/bin/python3

"""
    Module implementing the class square
"""


class Square:
    """
        square:
            Implementation of the class square
            """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialization method for instance attributes """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter method for the size instance """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for the size instance attribute """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Getter method for the position instance """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter method for the position  instance attribute """
        if not (isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integer")
        elif not (len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integer")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """ Method to compute and return the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ method to print the square using # """
        if not self.__size == 0:
            r = 0
            while r < self.__size:
                for i in range(self.__position[0]):
                    print(" ", end='')
                i = 0
                while i < self.__size:
                    print("#", end='')
                    i += 1
                print()
                r += 1
        else:
            print()
