#!/usr/bin/python3

""" Module which write to a file """


def write_file(filename="", text=""):
    """
        Function that opens a file with a
        write permission and write a given test to
        the file
    """
    with open(filename, "w", encoding="utf-8") as rep:
        ret = rep.write(text)
    return ret
