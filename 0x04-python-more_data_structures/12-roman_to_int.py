#!/usr/bin/python3

"""
    Module to get the number of integer equivalent
    of a given roman symbols of numeral
"""


def roman_to_int(roman_string):
    symb = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if type(roman_string) is str:
        rslt = 0
        i = 0
        while (i < len(roman_string)):
            if (i + 1) < (len(roman_string)):
                if symb[roman_string[i + 1]] > symb[roman_string[i]]:
                    rslt += symb[roman_string[i + 1]] - symb[roman_string[i]]
                    i = i + 1
                else:
                    rslt += symb[roman_string[i]]
            else:
                rslt += symb[roman_string[i]]
            i = i + 1
        return rslt
    else:
        return 0
