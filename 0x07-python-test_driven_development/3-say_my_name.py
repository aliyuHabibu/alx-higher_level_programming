#!/usr/bin/python3

"""
    Module to check for given string and
        print them as a nam
"""


def say_my_name(first_name, last_name=""):
    """
        This is the say my name function which print
            given string as a complete name
                args:
                    first_name: The first name given.
                    last_name: The last name given.
            If any of the variable given contain a value which
                    not a string or None, then raise an exception
                    """
    if not type(first_name) == str and not type(last_name) == str:
        raise TypeError("first_name must be a string")

    elif not type(first_name) == str:
        raise TypeError("first_name must be a string")

    elif not type(last_name) == str:
        raise TypeError("last_name must be a string")

    elif first_name is None:
        raise TypeError("first_name must be a string")

    elif last_name is None:
        raise TypeError("last_name must be a string")

    else:
        print(f"My name is {first_name} {last_name}")
