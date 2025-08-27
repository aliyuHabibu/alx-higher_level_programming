#!/usr/bin/python3

"""
    Function to print the keys with
    corresponding values of a given dictionay
"""


def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary)
    for i in range(len(sorted_dic)):
        print(f"{sorted_dic[i]}: {a_dictionary[sorted_dic[i]]}")
