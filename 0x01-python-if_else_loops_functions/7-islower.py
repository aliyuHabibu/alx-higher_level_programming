#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 122):
        if (c >= 'a') and (c <= 'z'):
            return True
        else:
            return False
