"""
Write the programm that calculate total price with discount by the products.

Use class Product(name, price, count) and class Cart. In class Cart you can add the products.

Discount depends on count product:


count	discount
at least 5	5%
at least 7	10%
at least 10	20%
at least 20	30%
more than 20	50%
Write unittest with class CartTest and test all methods with logic
"""

import unittest

class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        if 7 > self.count >= 5:
            self.discount = .95
        elif 10 > self.count >= 7:
            self.discount = .9
        elif 20 > self.count >= 10:
            self.discount = .8
        elif self.count == 20:
            self.discount = .7
        elif self.count > 20:
            self.discount = .5
        else: self.discount = 1
        self.cost = self.count * self.price * self.discount


class Cart:
    def __init__(self, product):
        self.order = list(product)
    
    def add_product(self, product):
        self.order.append(product)
    
    def get_total_price(self):
        total_cost = 0
        for product in self.order:
            total_cost += product.cost
        return total_cost

def total_price():
    products = []
    for count in range(30):
        products.append(Product(f"test_name_{count}", 100, count))
    cart = Cart(products)
    return cart.get_total_price()

class CartTest(unittest.TestCase):
    #input_count = (0, 1, 5, 6, 7, 9, 10, 19, 20, 21, 100)
    def test_discounts(self):
        self.assertEqual(total_price(), 28455.00)
