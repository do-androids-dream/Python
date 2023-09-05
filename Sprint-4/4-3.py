"""
Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. 

Each instance should have a name and a lastname attributes plus one more attribute for each of the keywords, if any.

Examples:
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
mary.lastname ➞ "Major"
richard.height ➞ 178
giancarlo.nationality ➞ "Italian"
john.name ➞ "John"
"""

class Employee:
    def __init__(self, full_name, **kwargs) -> None:
        self.name, self.lastname = full_name.split(" ")
        for k, v in kwargs.items():
            setattr(self, k, v)
        


john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
print(mary.lastname) #➞ "Major"
print(richard.height) #➞ 178
print(giancarlo.nationality) #➞ "Italian"
print(john.name) #➞ "John"