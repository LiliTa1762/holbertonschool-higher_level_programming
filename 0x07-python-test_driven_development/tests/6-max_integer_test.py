#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the function max_integer"""
    def test_max_int(self):
        """Test the max integer of a function"""
        list = []
        message = None
        self.assertIsNone(max_integer(list), message)


def test_one_element(self):
        """Tests for only one number in the list"""
        list = [1]
        self.assertEqual(max_integer(list), 1)


def test_positive_end(self):
        """Tests for all positive with max at end"""
        l = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(l), 50)


def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(m), 360)


if __name__ == '__main__':
    unittest.main()
