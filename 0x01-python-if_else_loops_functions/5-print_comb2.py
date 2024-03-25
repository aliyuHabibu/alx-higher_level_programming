#!/usr/bin/python3
for i in range(0, 10):
    for x in range(0, 10):
        print(f"{i}{x}", end='')
        if not ((i == 9) and (x == 9)):
            print(", ", end='')
print()
