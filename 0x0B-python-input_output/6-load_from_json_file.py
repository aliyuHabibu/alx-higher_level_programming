#!/usr/bin/python3

""" Loading from a json file """

# Imprting dependencies
import json


def load_from_json_file(filename):
    """
        Function that opens a json file,
        read from the file and convert the json object
        into a python object(Deserialization)
    """
    with open(filename) as rep:
        strg = rep.read()
        ret = json.loads(strg)
        return ret
