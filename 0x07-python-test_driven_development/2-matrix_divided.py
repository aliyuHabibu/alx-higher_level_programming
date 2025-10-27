#!/usr/bin/python3

"""
    Module to divide the element in a matrix
    by a specific value
    and return a new matrix of the divided value
"""


def matrix_divided(matrix, div):
    """
        The division function.
            args:
                matrix - The list containing elements
                div - value to divide with.
            All matrix element must be of type int
            Matrix must be a list of lists
            Division value must be an int and greater than zero
            """
    ret_list = [[], []]
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            if type(matrix[i][x]) not in [int, float]:
                raise TypeError('matrix must be a matrix of integers/float')

    i = 0
    while i < len(matrix):
        if not len(matrix[0]) == len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        i += 1

    if not type(div) in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for x in range(len(matrix)):
        i = 0
        while i < len(matrix[x]):
            ans = round(matrix[x][i]/div, 2)
            ret_list[x].append(ans)
            i += 1
    return ret_list
