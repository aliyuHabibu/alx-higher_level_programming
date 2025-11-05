#!/usr/bin/python3

""" A module which return a dictionary
    representation of all class attribute
"""


def class_to_json(obj):
    return obj.__dict__
