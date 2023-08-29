# try:
#     a = int(input("input int: "))
#     print(1 / a)
# except (ValueError, TypeError):
#     print("try again...")
# except ZeroDivisionError:
#     print("a-ta-ta!")
# except  AttributeError:
#     print("Such method is not available, so-o-o-orry...")
# except:
#     print("any othe exception caused...")


# try:
#     value = input("Введіть значення: ")
#     print(value/value)
# except ValueError:
#     print("Погане введення...")
# except ZeroDivisionError:
#     print("Дуже погане введення...")
# except TypeError:
#     print("Дуже, дуже погане введення…")
# except:
#     print("Бууу!")



# my_list = ['Mary', 'had', 'a', 'little', 'lamb']
 
# def my_listf(my):
#     #del my_list[3]
#     #my_list[3] = 'ram'
#     my.append(10)

# print(my_listf(my_list))
# print(my_list)


# dictionary = {'один': 'два', 'три': 'один', 'два': 'три'}
# v = dictionary['один']
 
# for k in range(len(dictionary)):
#     v = dictionary[v]
 
# print(v)


# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z
 
# print(x, y, z)


#print(ab, cd!)

def fun(nums, target):
    lst = []    
    for i in nums:
        if target - i in nums:
            i2 = target - i
            lst.append(nums.index(i))
            lst.append(nums.index(i2))
            break
    return lst

print(fun([1, 2, 3, 4, 5], 8))