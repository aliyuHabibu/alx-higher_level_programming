#!/usr/bin/python3

""" Using the json module"""

# Importing dependencies
import json


def to_json_string(my_obj):
    """
        Function that jsonify a
        given python data structure
        if it can be jsonified.
    """
    ret = json.dumps(my_obj, sort_keys=True)
    return ret
