"""
For the given integer n, consider an increasing sequence consisting of all positive integers that are either powers of n, or sums of distinct powers of n.

Your task is to find the kth (1-based) number in this sequence.

Example

For n = 3 and k = 4, the output should be
kthTerm(n, k) = 9.

For n = 3, the sequence described above begins as follows: 1, 3, 4, 9, 10, 12, 13...
[3**0] => [1]
[1, 3**1, 3**1 +1] => [1, 3, 4]
[1, 3, 4, 3**2, 3**2 +1, 3**2 +3, 3**2 +4] => [1, 3, 4, 9, 10, 12, 13]
...

The 4th number in this sequence is 9, which is the answer.

Input/Output

[input] integer n

The number to build the sequence by.

Constraints:
2 ≤ n ≤ 30.

[input] integer k

The 1-based index of the number in the sequence.

Constraints:
1 ≤ k ≤ 100.

[output] integer

The kth element of the sequence.
"""

# def kthTerm(n, k):
#     lst = [1]
#     count = 0
#     while len(lst) <= k:
#         lst2 = lst[:]
#         count += 1
#         lst2.append(n ** count)
#         for i in lst:
#             lst2.append(n ** count + i)
#         lst = lst2
#     return lst[k - 1]

def kthTerm(n, k):
    lst = [1]
    count = 0
    while len(lst) < k:
        count += 1
        lst2 = [n ** count + i for i in lst]
        lst.append(n ** count)
        lst.extend(lst2)
    #print(lst)
    return lst[k - 1]

print(kthTerm(3, 4))



