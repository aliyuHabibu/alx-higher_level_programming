#!/usr/bin/python3

"""
    Function to delete or remove a key/value
    from a given dictionary
"""


def simple_delete(a_dictionary, key=""):
    sorted_dic = sorted(a_dictionary)
    for i in range(len(a_dictionary)):
        if sorted_dic[i] == key:
            del a_dictionary[key]
    return a_dictionary
