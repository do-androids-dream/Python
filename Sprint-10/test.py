# s = [1,]
# print(bool(s))


# def arrange(s):
#     length = len(s)
#     ind = 0
#     x = s[:]
#     t = [None for i in range(length)]
#     while bool(x):
#         print(x)
#         t[ind] = (x.pop(0))
#         ind += 1
#         if bool(x):
#             t[ind] = (x.pop())
#             ind += 1
#         x = x[::-1]
#     return t

# print(arrange([9, 7, -2, 8, 5, -3, 6, 5, 1])) #[9, 1, 5, 7, -2, 6, -3, 8, 5]

# def arrange(s):
#     length = len(s)
#     if not s:
#         return []
#     elif length < 3:
#         return s[:]
#     else:
#         start = s[0]
#         middle = s[::-1][1:-1]
#         end = s[-1]
#         #print(start, middle, end)
#         t = [start] + [end] + arrange(middle)
#     return t

# print(arrange([9, 7, -2, 8, 5, -3, 6, 5, 1])) #[9, 1, 5, 7, -2, 6, -3, 8, 5]
# print(arrange([1,2])) #[1,2]
# print(arrange([2, 4, 3, 4])) #[2, 4, 3, 4]
# #print(arrange())

# def arrange(s):
#     length = len(s)
#     t = [None for i in range(length)]
#     ind = 0
#     start = 0
#     end = -1
#     go = True
#     while go:
#         if length:
#             t[ind] = s[start]
#             start += 1
#             ind += 1
#             length -= 1
            
#         else: go = False
#         if length:
#             t[ind] = s[end]
#             ind += 1
#             end -= 1
#             length -= 1
            
#         else: go = False
#         if length:
#             t[ind] = s[end]
#             end -= 1
#             ind += 1
#             length -= 1
            
#         else: go = False
#         if length:
#             t[ind] = s[start]
#             start += 1
#             ind += 1
#             length -= 1
            
#         else: go = False
#     return t

# print(arrange([9, 7, -2, 8, 5, -3, 6, 5, 1])) #[9, 1, 5, 7, -2, 6, -3, 8, 5]
# print(arrange([1,2])) #[1,2]
# print(arrange([2, 4, 3, 4])) #[2, 4, 3, 4]

# def gen_array():
#     start = 0
#     end = -1
#     while True:
#         yield start
#         start += 1
#         yield end
#         end -= 1
#         yield end
#         end -=1
#         yield start
#         start += 1

# def arrange(s):
#     return [s[ind] for ind, el in zip(gen_array(), s)]

# print(arrange([9, 7, -2, 8, 5, -3, 6, 5, 1])) #[9, 1, 5, 7, -2, 6, -3, 8, 5]
# print(arrange([1,2])) #[1,2]
# print(arrange([2, 4, 3, 4])) #[2, 4, 3, 4]

for i in range(20):
    print(bin(~i))