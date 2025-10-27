#!/usr/bin/python3

"""Unittest for max_integer([..])
"""

# Importing dependencies
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, 5j)
        self.assertRaises(TypeError, max_integer, "Me")
