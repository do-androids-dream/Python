"""
Create class Triangle with method get_area() that calculate area of triangle. 
As input you will have list of 3 sides size
Examples:
triangle = Triangle([3, 3, 3])
Use classes TriangleNotValidArgumentException and TriangleNotExistException

Create class TriangleTest with unittest and subTest() context manager for class Triangle. 
test data:
valid_test_data = [
    ((3, 4, 5), 6.0),
    ((10, 10, 10), 43.30),
    ((6, 7, 8), 20.33),
    ((7, 7, 7), 21.21),
    ((50, 50, 75), 1240.19),
    ((37, 43, 22), 406.99),
    ((26, 25, 3), 36.0),
    ((30, 29, 5), 72.0),
    ((87, 55, 34), 396.0),
    ((120, 109, 13), 396.0),
    ((123, 122, 5), 300.0)
]
not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]
not_valid_arguments = [
    ('3', 4, 5),
    ('a', 2, 3),
    (7, "str", 7),
    ('1', '1', '1'),
    'string',
    (7, 2),
    (7, 7, 7, 7),
    'str',
    10,
    ('a', 'str', 7)
]
"""

import unittest

class TriangleNotValidArgumentException(Exception):
    def __str__(self):
        return "Not valid arguments"


class TriangleNotExistException(Exception):
    def __str__(self):
        return "Can`t create triangle with this arguments"


class Triangle:
    def __init__(self, data):
        try:
            if len(data) != 3:
                raise TriangleNotValidArgumentException
        except TypeError:
            raise TriangleNotValidArgumentException
        for item in data:
            if isinstance(item, str):
                raise TriangleNotValidArgumentException

        self.a, self.b, self.c = data
        if (self.a + self.b <= self.c) or\
            (self.b + self.c <= self.a) or\
            (self.c + self.a <= self.b):
            raise TriangleNotExistException

    def get_area(self):
        s = .5 * (self.a + self.b + self.c)
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** .5
        return area

# not_valid_arguments = [
#     ('3', 4, 5),
#     ('a', 2, 3),
#     'string',
#     (7, 2),
#     (7, 7, 7, 7),
#     10
# ]
# for data in not_valid_arguments:
#     print(*data)
#     try:
#         Triangle(data)
#     except TriangleNotExistException as e:
#         print(e)

class TriangleTest(unittest.TestCase):
    valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
    
    def test_t(self):
        for data in TriangleTest.valid_test_data:
            with self.subTest():
                t = Triangle(data[0])
                self.assertAlmostEqual(t.get_area(), data[-1], delta=0.01)

    def test_1(self):
        self.assertIsNotNone(Triangle((3, 4, 5)))

    def test_3(self):
        t = Triangle((10, 10, 10))
        self.assertAlmostEqual(t.get_area(), 43.30, delta=0.01)
    