"""
Generator function randomWord has as an argument list of words. It should return any random word from this list. Each time words are different until the end of the list is reached. 
Then words are taken from the initial list again.


For example if 

list = ['book', 'apple', 'word']

books = randomWord(list)

then possible output example 

first call of next(books) returns apple

second call of next(books) returns book

third call of next(books) returns word

fourth call of next(books) returns book
"""
import random

def randomWord(lst):
    while len(lst):
        lst2 = lst[:]
        count = len(lst2)
        result = random.sample(lst2, len(lst2))
        for i in result:
            yield i
    else:
        while True:
            yield None

list = ['book', 'apple', 'word']

books = randomWord(list)

print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print()
list1 = []
list2 = []
for i in range(len(list)):
    list1.append(next(books))
for i in range(len(list)):
    list2.append(next(books))
print(list1, list2)
print(list1!=list2)
print()
empty = randomWord([])
print(next(empty))
print(next(empty))