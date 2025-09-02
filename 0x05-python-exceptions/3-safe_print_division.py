#!/usr/bin/python3

"""
    Function to safely divide two given integer
    and also handle division exceptions.
"""


def safe_print_division(a, b):
    try:
        a / b
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        if b == 0:
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {}".format(a / b))
