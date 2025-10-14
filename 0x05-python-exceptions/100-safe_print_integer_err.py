#!/usr/bin/python3

"""
    Module to print integer and also print
    to stderr when not an integer is passed
"""

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        sys.stderr.write(f"Exception: {e}\n")
        return False
