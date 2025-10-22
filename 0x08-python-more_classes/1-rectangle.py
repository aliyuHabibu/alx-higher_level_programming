#!/usr/bin/python3

"""
    Module that define the class rectangle
"""


class Rectangle:
    """
        Definition of the class rectangle
    """
    def __init__(self, width=0, height=0):
        "Initialization method for all object variables"
        self.height = height
        self.width = width

    @property
    def height(self):
        "The getter method for the height instance variable"
        return self.__height

    @height.setter
    def height(self, value):
        "The setter method for the height instance variable"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    @property
    def width(self):
        "Getter method for width instance variable"
        return self.__width

    @width.setter
    def width(self, value):
        "Stter method for width instance variable"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value
