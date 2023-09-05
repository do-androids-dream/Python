class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def display(self):
        print(self.name, self.__age)


person = Person("VD", 35)

person.display()

print(person._Person__age) #direct access to mangled aatribute
#print(person.__age) #will cause error, because internally name was changed to self._Class__atribute

#property method getter, setter, deleter, doc
class Test:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self.__c = c
    
    def print_self(self):
        print(self)

    def __get_a(self):
        return self._a
    
    def __set_a(self, new_value):
        if new_value > 0:
            self._a = new_value
            print("new value was applied, a=", self._a)
        else: print("cannot be negetive")
    
    def __get_b(self):
        return self._b
    
    def __set_b(self, new_value):
        if new_value < 100:
            self._b = new_value
            print("new value for b is set, b=", self._b)
        else: print("should be less then 100")
    
    def __get__c(self):
        return self.__c
    
    a_value = property(__get_a, __set_a)
    b = property(__get_b, __set_b)
    c = property(__get__c)

t1 = Test(1, 2, 3)
t2 = Test(10, 20, 30)

print(t1.a_value)
t1.a_value = 55
t2.b = 100
print(t1.b, t2.b)
print(t1._a)
print(t2._Test__c)
print(t2.c)

t1.print_self()

lst = []
print(lst[-1])