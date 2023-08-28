# test_list = [['99'], ['88'], ['77'], ['66']] 
# res = [[int(i) for i in sub] for i in test_list for sub in i]  

# print("The list after conversion: " + str(res)) 


# l1 = [[10, 20], [30, 40], [50, 60]] 
# ls = list(l1)
# print(ls)


# my_dict = {'A': ['A', 'B'], ('A',): 'A'}
# print(my_dict)


# x = 3 
# print((x<<2) + 1)


# print(55 == '55')


# test_list = [['99'], ['88'], ['77'], ['66']] 
# res = [[int(i) for i in sub] for i in test_list for sub in i] 
# print(res)

# for i in test_list:
#     print(i)
#     for sub in i:
#         print(sub)
#         res = [int(i) for i in sub]
#         print(res)

# test_list = [['99'], ['88'], ['77'], ['66']] 
# res = [[int(i) for i in sub] for i in test_list for sub in i] 


# def my_function(my_list_1):
#     print("Роздрукувати #1:", my_list_1)
#     print("Роздрукувати #2:", my_list_2)
#     my_list_1[0] = [0, 1]
#     print("Роздрукувати #3:", my_list_1)
#     print("Роздрукувати #4:", my_list_2)
 
 
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Роздрукувати #5:", my_list_2)
 

# def move_zeros(lst):
#     count = lst.count(0)
#     for i in range(count):
#         lst.remove(0)
#     for i in range(count):
#         lst.append(0)
#     return lst

# def move_zeros(lst):
#     ls = [i for i in lst if i] + [0] * lst.count(0)
#     return ls

# print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))


# def balanced_num(number):
#     number = str(number)
#     num1, num2 = 0, 0
#     if len(number) % 2 == 0:
#         for i in range(len(number) // 2 - 1):
#             num1 += int(number[i])
#         for i in range(len(number) // 2 + 1, len(number)):
#             num2 += int(number[i])
#     else:
#         for i in range(len(number) // 2):
#             num1 += int(number[i])
#         for i in range(len(number) // 2 + 1, len(number)):
#             num2 += int(number[i])
#     return "Balanced" if num1 == num2 else "Not Balanced"

# print(balanced_num(1024))


## List of perfect squaers!!!
# def off(n):
#     lst = [1 for i in range(1, n+1)]
#     count = 0
#     step = 0
#     start = 0
#     while count < n:
#         count += 1
#         step += 1
#         print(lst, count)
#         for i in range(start, n, step):
#             if lst[i] == 1: lst[i] = 0 
#             else: lst[i] = 1
#         start += 1
#     lst2 =[]
#     for i in range(n):
#         if lst[i] == 0: lst2.append(i+1)
#     return lst2

def off(n):
    return [i * i for i in range(1, int(n ** 0.5) + 1)]

print(off(9))