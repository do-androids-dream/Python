# for i in range(10):
#     a = i

# print(a)

# if True:
#     block_var = 10  # block_var is local to the if block

# print(block_var)  # Raises a NameError because block_var is not accessible here


# my_list = [x for x in range(5)]  # x is local to the list comprehension

# #print(x)  # Raises a NameError because x is not accessible here


# with open('1.json', 'r') as file:
#     file_content = file.read() 

# print(file_content)  
# print(file)


# #############################

# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     def __init__(self, shape_type):
#         self.shape_type = shape_type

#     @abstractmethod
#     def calculate_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("circle")
#         self.radius = radius

#     def calculate_area(self):
#         return pi * self.radius**2

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__("rectangle")
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height

# class Square(Shape):
#     def __init__(self, side):
#         super().__init__("square")
#         self.side = side

#     # def calculate_area(self):
#     #     return self.side**2

# class Square_2(Square):
#     def __init__(self, side):
#         super().__init__("square_2")
#         self.side = side

#     def calculate_area(self):
#         return self.side**2

# sq = Square_2(5)
# print(sq.calculate_area())

# rt = Rectangle(5, 2)
# print(rt.calculate_area())


#########
##Abstract Factory
#from abc import ABC, abstractmethod
import abc

class Abstract_factory(abc.ABC):
    @abc.abstractmethod
    def create_A(self):
        pass

    @abc.abstractmethod
    def create_B(self):
        pass

class Factory_1(Abstract_factory):
    def create_A(self):
        return Product_A1()

    def create_B(self):
        return Product_B1()

class Factory_2(Abstract_factory):
    def create_A(self):
        return Product_A2()

    def create_B(self):
        return Product_B2()

class Product_A(abc.ABC):
    @abc.abstractmethod
    def some_method_a(self):
        pass

class Product_B(abc.ABC):
    @abc.abstractmethod
    def some_method_b(self):
        pass

class Product_A1(Product_A):
    def some_method_a(self):
        return "Result A1"

class Product_A2(Product_A):
    def some_method_a(self):
        return "Result A2"

class Product_B1(Product_B):
    def some_method_b(self):
        return "Result B1"

class Product_B2(Product_B):
    def some_method_b(self):
        return "Result B2"

product_1 = Factory_1()
product_2 = Factory_2()
result_a1 = product_1.create_A()
result_b2 = product_2.create_B()
result_a2 = Factory_2().create_A()
print(result_a1.some_method_a())
print(result_b2.some_method_b())
print(result_a2.some_method_a()) 