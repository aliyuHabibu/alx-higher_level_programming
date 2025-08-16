#!/usr/bin/python3
i = ord('z')
while i >= ord('a'):
    print("{:c}".format(i) if i % 2 == 0 else "{:c}".format(i-32), end='')
    i = i - 1
