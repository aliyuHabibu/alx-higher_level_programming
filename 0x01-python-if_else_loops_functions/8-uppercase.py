#!/usr/bin/python3
def uppercase(str):
    for i in str:
        #print(i)
        print("{}".format(i) if ord(i) < 90 else "{:c}".format(ord(i)-32), end='')
    print()
