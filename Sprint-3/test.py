# def func(a=0, *args, **kwargs):
#     print(a)
#     print(args)
#     print(kwargs)

# func(1, 2, 3, 4, 5, 6, a1 = 1, b = 2, c = 3)

# ## lambda
# y = 3
# print((lambda x: x * 2) (y))

# ## closure
# def clos(name):
#     return lambda: print("Hi,", name)

# jack = clos("Jack")
# dima = clos("Dima")

# jack()
# dima()


# def test(name):
#     def test2():
#         print("Test2", name)
#     return test2

# t = test("TEST")

# t()

# ## global space, local and non-local space
# text = "text" # global

# def test_print():
#     text = "text2" # non-local
#     def try_print():
#         print(text) #local
#     try_print()

# test_print()


# ## functional programming
# names = ["a", "b", "c"]
# for i in range(len(names)):
#     names[i] = hash(names[i])
# print(names)

# names = ["a", "b", "c"]
# names = [hash(i) for i in names]
# print(names)

# names = ["a", "b", "c"]
# names = map(lambda name: hash(name), (names))
# print(list(names))

# names = ["a", "b", "c"]
# names = map(hash, names)
# print(list(names))


# from functools import reduce
# numbers = [1, 2, 22, -10, 15, 99, 55, 5]
# max_number = reduce(lambda a, b: a if a > b else b, numbers)
# print(max_number)


# ## generator
# def gen(n):
#     for i in range(n):
#         yield i

# print(gen(5))
# g = gen(10)
# print(g)

# print(next(g))
# print(next(g))
# print(next(g))
# print(type(next(g)))


# def iterat(n):
#     return range(n)

# print(type(iterat(5)))


# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2

# for v in powers_of_2(8):
#     print(v)


# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2

# for i in range(20):
#     if i in powers_of_2(4):
#         print(i)


# for i in [i * 2 for i in range(1,11)]:
#     print(i)

# for i in (i * 2 for i in range(1, 11)):
#     print(i)

# lst = [i for i in range(1, 11)]
# print(dir(lst))
# print()
# string = "abcde"
# print(dir(string))
# print()
# integer = 1000
# print(dir(integer))

gen = (i * 2 for i in range(1,11))
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# ## for in
# # Behind the scenes, this is equivalent to manually using an iterator and next() function:
# my_list = [1, 2, 3, 4, 5]
# my_iterator = iter(my_list)
# while True:
#     try:
#         item = next(my_iterator)
#         print(item)
#     except StopIteration:
#         break


