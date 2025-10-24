#!/usr/bin/python3

"""
    Module that define a class rectangle
"""


class Rectangle:
    """
        Definition of the class rectangle
    """

    hashes = "#"

    def __init__(self, width=0, height=0):
        """Initialization method or all instances"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter methioed for width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width instance attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height instance attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an nteger")

        if value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    def area(self):
        """Method that compute and return the area of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * self.__height

    def perimeter(self):
        "Method that compute and return the perimeter of a rectangle"
        return 2 * (self.__width + self.__height)

    def __str__(self):
        "Method that return a string rep of class instances"
        if self.__height == 0 or self.__width == 0:
            return ""

        for i in range(self.__height):
            for x in range(self.__width):
                print("#", end='')
            if not i == self.__height - 1:
                print()
        return ""

    def __repr__(self):
        "Method that return an executable string rep of class instances"
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        "Method that handles deletion when called upon a class instance"
        print("Bye rectangle...")
