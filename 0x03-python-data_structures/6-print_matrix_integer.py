#!/usr/bin/python3

"""
    Function to print element of a matrix
"""


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if not len(matrix[i]) == 0:
            x = 0
            for x in range(len(matrix)):
                print("{}".format(matrix[i][x]), end='')
                if not x == len(matrix[i]) - 1:
                    print("{}".format(' '), end='')
        print("{}".format('\n'), end='')
