#!/usr/bin/python3
import sys
args = (len(sys.argv) - 1)
if args == 0:
    print(f"{args} arguments.")
else:
    print(f"{args} argument:")
    i = 1
    while i <= args:
        print(f"{i}: {sys.argv[i]}")
        i += 1

__name__ == "__main__"
