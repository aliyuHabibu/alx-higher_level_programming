#!/usr/bin/python3

""" This Module append to the end of the file without truncating """


def append_write(filename="", text=""):
    """
        Function to open a file with a
        write permission and append a given
        text to the file.
    """
    with open(filename, "a") as rep:
        ret = rep.write(text)
    return ret
