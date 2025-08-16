#!/usr/bin/python3
def remove_char_at(str, n):
    copy = str[:]
    for i in range(len(str)):
        if n < 0 or n > len(str):
            return copy
        else:
            if i == n:
                lt = list(copy)
                lt[i] = ''
                return ''.join(lt)
