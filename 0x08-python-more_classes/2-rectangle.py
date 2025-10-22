#!/usr/bin/python3

"""
    Module that defines a class rectangle
    with a getter and setter method and
    some additional methods
"""


class Rectangle:
    """
        Definition of the class rectangle
    """
    def __init__(self, width=0, height=0):
        "Initialization method or all instances"
        self.height = height
        self.width = width

    @property
    def width(self):
        "Getter method for the width instance variable"
        return self.__width

    @width.setter
    def width(self, value):
        "setter method for width instance variable"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        "Getter nethod for height instance variable"
        return self.__height

    @height.setter
    def height(self, value):
        "Setter method for height instance variable"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    def area(self):
        "Method to get and return the 'Area' of a rectnagle"
        return self.__height * self.__width

    def perimeter(self):
        "Method to get and return the 'Perimeter' of a rectangle"
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
