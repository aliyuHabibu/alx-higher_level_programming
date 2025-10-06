#!/usr/bin/python3

"""
    Function to count and return a tuple
    of number of characters given and also
    the furst letter
"""


def multiple_returns(sentence):
    n = 0
    if len(sentence) == 0:
        return (n, None)
    else:
        for i in range(len(sentence)):
            n += 1
        return (n, sentence[0])
