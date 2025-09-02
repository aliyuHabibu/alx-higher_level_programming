#!/usr/bin/python3

"""
    Script to count and read arguments from
    command line and print to the stdout
"""

import sys

args = (len(sys.argv) - 1)

if __name__ == "__main__":
    if args == 0:
        print(f"{args} arguments.")
    elif args == 1:
        print(f"{args} argument:")
        print(f"{args}: {sys.argv[args]}")
    else:
        print(f"{args} arguments:")
        i = 1
        while i <= args:
            print(f"{i}: {sys.argv[i]}")
            i += 1
