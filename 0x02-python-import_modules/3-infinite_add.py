#!/usr/bin/python3

"""
    Script to sum all numbers privided as argument
    from the standard input.
"""

from sys import argv

args = (len(argv) - 1)
ans = 0

if __name__ == "__main__":
    if args == 0:
        print(ans)
    else:
        i = 1
        while i <= args:
            ans += int(argv[i])
            i += 1
        print(ans)
