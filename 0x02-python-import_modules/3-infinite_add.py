#!/usr/bin/python3
from sys import argv
args = (len(argv) - 1)
ans = 0
if args == 0:
    print(ans)
else:
    i = 1
    while i <= args:
        ans += int(argv[i])
        i += 1
    print(ans)
