#!/usr/bin/python3

"""
    Function to multiply each element of a
    double list by itself and return the list
    of list
"""


def square_matrix_simple(matrix=[]):
    my_matrix = matrix.copy()
    list_of_list = []
    for i in range(len(my_matrix)):
        list_of_ele = []
        for x in range(len(my_matrix)):
            ans = my_matrix[i][x] * my_matrix[i][x]
            list_of_ele.append(ans)
        list_of_list.append(list_of_ele)
    return list_of_list
