#!/usr/bin/python3

"""
    Module that implement a class and a function
    that is serializable
"""


class Student:
    "Class Definition"
    def __init__(self, first_name, last_name, age):
        "Initialization method for all class instances"
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        "Method to return a dict rep of the class attributes"
        return self.__dict__
