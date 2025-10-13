#!/usr/bin/python3

"""
    Function to divide all elements of a given list
    and return a list containing the answers
"""


def list_division(my_list_1, my_list_2, list_length):
    list_ans = []
    i, ans = 0, 0
    while i < list_length:
        try:
            ans = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError as ze:
            print("division by 0")
        except TypeError as ty:
            print("wrong type")
        except IndexError as ix:
            print("out of range")
        finally:
            if ans == 0:
                list_ans.append(ans)
            else:
                list_ans.append(ans)
                ans = 0
        i += 1
    return list_ans
