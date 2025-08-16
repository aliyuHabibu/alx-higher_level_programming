#!/usr/bin/python3

from test import 
def magic_calculation(a, b):
    """
        Function to practice python bytecode
    """
    return 98 + a ** b

import dis
print(dis.dis(magic_calculation))
