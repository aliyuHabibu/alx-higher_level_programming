#!/usr/bin/python3

"""
    Module to safely execute a given unction and
    return the function return value
"""
import sys


def safe_function(fct, *args):
    try:
        rst = fct(args[0], args[1])
        return rst
    except Exception as e:
        sys.stderr.write(f"Exception: {e}\n")
        return None
