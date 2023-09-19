"""
Write the function quadratic_equation with arguments a, b ,c that solution to quadratic equation 
without a complex solution.

Write unit tests for this function with QuadraticEquationTest class

Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0
"""

import unittest


def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError
    discriminant = b**2 - 4*a*c
    print(discriminant)
    if discriminant > 0:
        root1 = (-b + (discriminant)**.5) / (2*a)
        root2 = (-b - (discriminant)**.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root1 = (-b + (discriminant)**.5) / (2*a)
        return root1
    else:
        return None

# print(quadratic_equation(2, 1, -1))
print(quadratic_equation(1, -4, 4))


class QuadraticEquationTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(quadratic_equation(2, 1, -1), (0.5, -1.0))

    def test_2(self):
        self.assertEqual(quadratic_equation(4, 1, 2), None)

    def test_3(self):
        self.assertIsNone(quadratic_equation(4, 1, 2))
    
    def test_4(self):
        self.assertGreater(quadratic_equation(1, -4, 4), 0)