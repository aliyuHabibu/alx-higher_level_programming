#!/usr/bin/python3

"""
    Module that defines class Rectangle
"""


class Rectangle:
    """
        Definition of class Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization method or all instances"""
        Rectangle.number_of_instances += 1
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

    @classmethod
    def __str__(cls):
        "Method that return a string rep of class instances"
        if cls.height == 0 or cls.width == 0:
            return ""

        for i in range(cls.height):
            for x in range(cls.width):
                print("{}".format(cls.print_symbol), end='')
            if not i == cls.height - 1:
                print()
        return ""

    def __repr__(self):
        "Method that return an executable string rep of class instances"
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        "Method that handles deletion of class instances"
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Method check the area of two given instances of the class
        and return the instances with the greater area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1

        if rect_1.area() > rect_2.area():
            return rect_1

        if rect_1.area() < rect_2.area():
            return rect_2
