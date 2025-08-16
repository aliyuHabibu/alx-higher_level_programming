#!/usr/bin/python3
for i in range(0, 100):
        print("0{}, ".format(i) if i < 10 else "{}, ".format(i) if not i == 99 else "{}".format(i), end='')
print()
        
