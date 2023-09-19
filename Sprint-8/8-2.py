"""
You have function divide
def divide(num_1, num_2):
    return float(num_1)/num_2
Please, write the code with unit tests for the function "divide":
minimum 3 tests
must chek all flows
all test must be pass
no failures
no skip
"""

def divide(num_1, num_2):
    return float(num_1)/num_2

import unittest

class DivideTest(unittest.TestCase):
    def test_edge(self):
        result = divide(100, 100)
        expected = 1.0
        self.assertEqual(result, expected)

    def test_zero(self):
        self.assertRaises(Exception, divide, 100, 0)

    def test_wrong_input(self):
        self.assertRaises(Exception, divide, "abc", 10)