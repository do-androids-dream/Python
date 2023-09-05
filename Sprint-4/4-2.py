"""
Create a Pizza class with the attributes order_number and ingredients (which is given as a list). 
Only the ingredients will be given as input.

You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the ingredients manually! 
As well as creating this Pizza class, hard-code the following pizza flavours.

Examples:
p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
p2 = Pizza.garden_feast()                  # order 2
p1.ingredients ➞ ["bacon", "parmesan", "ham"]
p2.ingredients ➞ ["spinach", "olives", "mushroom"]
p1.order_number ➞ 1
p2.order_number ➞ 2
"""

class Pizza:
    order = 0
    def __init__(self, ingredients = None) -> None:
        Pizza.order += 1
        self.order_number = Pizza.order
        self._ingredients = ingredients

    def __get_ingredients(self):
        return self._ingredients

    def hawaiin():
        return Pizza(["ham", "pineapple"])

    def meat_festival():
        return Pizza(["beef", "meatball", "bacon"])
    
    def garden_feast():
        return Pizza(["spinach", "olives", "mushroom"])

    ingredients = property(__get_ingredients)
    # hawaiin = property(__set_hawaiin)
    # meat_festival = property(__set_meatfestival)
    # garden_feast = property(__set_garden_feast)

p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
p2 = Pizza.garden_feast()                  # order 2
print(p2)
print(p1.ingredients, p1.order_number) #➞ ["bacon", "parmesan", "ham"]
print(p2.ingredients, p2.order_number) #➞ ["spinach", "olives", "mushroom"]
