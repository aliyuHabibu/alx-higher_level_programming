#!/usr/bin/python3

"""
    Script to handle input from the command line, arguments
    and appropraitely perform operation and print to the screen.
"""

# Importimg Dependencies
from calculator_1 import add, sub, div, mul
from sys import argv


def print_to_screen(num1, oper, num2, func):
    """
        Function to print answer to the screen
    """
    print("{} {} {} = {}".format(num1, oper, num2, func(int(num1), int(num2))))


if __name__ == "__main__":
    oper = ['+', '-', '*', '/']
    if not len(argv) == 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in oper:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if oper[0] == argv[2]:
            print_to_screen(argv[1], oper[0], argv[3], add)
        elif oper[1] == argv[2]:
            print_to_screen(argv[1], oper[1], argv[3], sub)
        elif oper[2] == argv[2]:
            print_to_screen(argv[1], oper[2], argv[3], mul)
        elif oper[3] == argv[2]:
            print_to_screen(argv[1], oper[3], argv[3], div)
