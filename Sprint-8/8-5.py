"""
Create class Worker with fields name and salary. If salary negative raise ValueError

Create a method get_tax_value() that calculate tax from salary . Tax must be calculate like 
"progressive tax" with next step:

less then 1000 - 0%
1001 - 3000 - 10%
3001 - 5000 - 15%
5001 - 10000 - 21%
10001 - 20000 - 30%
20001 - 50000 - 40%
more than 50000 - 47%
Please create WorkerTest class with unitest to the class Worker. Try to use setUp and tearDown methods. 
Don`t use assertRaises in tests.
"""

import unittest

class Worker:
    def __init__(self, name, salary=0):
        if salary < 0:
             raise ValueError
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        if self.salary >= 50000:
            self.tax = (self.salary - 50000) * 0.47 + 30000 * 0.4 + 10000 * 0.3 + 5000 * 0.21 + 2000 * 0.15 + 2000 * 0.1
        elif 50000 > self.salary >= 20001:
            self.tax = (self.salary - 20000) * 0.4 + 10000 * 0.3 + 5000 * 0.21 + 2000 * 0.15 + 2000 * 0.1
        elif 20000 > self.salary >= 10001:
            self.tax = (self.salary - 10000) * 0.3 + 5000 * 0.21 + 2000 * 0.15 + 2000 * 0.1
        elif 10000 > self.salary >= 5001:
            self.tax = (self.salary - 5000) * 0.21 + 2000 * 0.15 + 2000 * 0.1
        elif 5000 > self.salary >= 3001:
            self.tax = (self.salary - 3000) * 0.15 + 2000 * 0.1
        elif 3000 > self.salary >= 1001:
            self.tax = (self.salary - 1000) * 0.1
        else:
            self.tax = 0
        return self.tax

worker = Worker("Vika", 100000)
print(worker.get_tax_value())

class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Valera", 1050)
        self.worker_2 = Worker("Nina", 500000)

    def test_1(self):
        self.assertGreater(self.worker_2.get_tax_value(), self.worker.get_tax_value())

    @unittest.expectedFailure
    def test_2(self):
        self.assertEqual(self.worker.get_tax_value(), 0)

    def tearDown(self):
        self.worker = None
        self.worker_2 = None
        