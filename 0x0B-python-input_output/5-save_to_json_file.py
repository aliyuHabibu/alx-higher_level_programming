#!/usr/bin/python3

""" Saving json string into a file """

# Importing dependencies
import json


def save_to_json_file(my_obj, filename):
    """
        Function that opens a file with write permission,
        jsonify a given python object and write it to
        the given file
    """
    with open(filename, "w") as rep:
        wrt = json.dumps(my_obj, sort_keys=True)
        rep.write(wrt)
