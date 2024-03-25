#!/usr/bin/python3

for i in range(0, 9):
    for x in range(1, 10):
        if x > i:
            print("{}{}".format(i, x), end='')
            if not ((i == 8) and (x == 9)):
                    print(", ",end='')
        else:
            continue
print()
