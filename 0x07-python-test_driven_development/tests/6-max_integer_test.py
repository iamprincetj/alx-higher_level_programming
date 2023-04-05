#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    '''Justin's Test for the max_integer function'''

    def test_first_num(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_num(self):
        self.assertEqual(max_integer([-5, -6, -2, -4]), -2)

    def test_zero_num(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_big_list(self):
        self.assertEqual(max_integer([
            1, 2, 5, 5, 6, 8, 524, 458,
            15, 16, 500, 800, 10000, 24150, 0, 524]), 24150)

    def test_all_same_num(self):
        self.assertEqual(max_integer([10, 10, 10, 10, 10]), 10)

    def test_for_string(self):
        with self.assertRaises(TypeError):
            max_integer(["50", 1, 50])

    def test_for_tuple_not_list(self):
        with self.assertRaises(TypeError):
            max_integer([(1, 2, 25), 54])

    def test_for_num_not_list(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_for_float(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 5.5, 6.1, 4.5]), 6.1)
