#!/usr/bin/python3

""" Convert from json string """

# Importing dependencies
import json


def from_json_string(my_str):
    """
        Function that returns a python data
        structure from a given valid json object
    """
    ret_json = json.loads(my_str)
    return ret_json
