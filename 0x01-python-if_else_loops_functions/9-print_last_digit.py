#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        i = abs(number) % 10
        print(f"{i}", end='')
        return i
    else:
        i = number % 10
        print(f"{i}", end='')
        return i
