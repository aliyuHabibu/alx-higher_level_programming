#!/usr/bin/python3

""" Module which prints the content of a
        file pass to it as arguement
"""


def read_file(filename=""):
    """
        Function that opens a file with
        a read permission and read from the file
        to the standard output.
    """
    with open(filename, encoding="utf-8") as rep:
        for char in rep:
            print(char, end='')
