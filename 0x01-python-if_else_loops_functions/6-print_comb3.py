#!/usr/bin/python3

for i in range(0, 9):
    for x in range(1, 10):
        if x > i:
            print(f"{i}{x}, ", end='')
        else:
            continue
