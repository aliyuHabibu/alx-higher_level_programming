#!/usr/bin/python3

""" This is a script that takes args from command line, save it
        to a list and save it in a json file
"""

# Importing dependencies
from sys import argv
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

try:
    loading = load_from_json("add_item.json")
    n = 1
    while n < len(argv):
        loading.append(argv[n])
        n = n + 1
    save_to_json(loading, "add_item.json")
except FileNotFoundError:
    save_to_json([], "add_item.json")
