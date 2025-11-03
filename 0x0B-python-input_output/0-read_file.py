#!/usr/bin/python3

""" Module which prints the content of a
        file pass to it as arguement
"""


def read_file(filename=""):
    with open(filename) as rep:
        for char in rep:
            print(char, end='')
