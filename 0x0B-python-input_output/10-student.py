#!/usr/bin/python3

"""
    Module that define a class with an intiliazation
    method and a method to return the dict of instances
"""


class Student:
    "Student class definition"
    def __init__(self, first_name, last_name, age):
        "Initialization method for all class instances"
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        "Method a return a dict rep of class instances"
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for attr in attrs:
                try:
                    my_dict[attr] = getattr(self, attr)
                except AttributeError:
                    continue
            return my_dict
