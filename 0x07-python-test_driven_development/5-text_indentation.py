#!/usr/bin/python3

"""
    Module to print character to
        the screen by printing each one
            at a time
"""


def text_indentation(text):
    """
        This is the function which print the character
            args:
                text - The text to extract from and print.
        If the text is not a type string and also None
                then it should raise an exception
                """
    if not type(text) == str:
        raise TypeError("text must be a string")

    elif text is None:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(f"{text[i]}")
            print()
        else:
            print("{}".format(text[i]), end='')
        i += 1
