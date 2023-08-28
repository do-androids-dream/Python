"""
Given two permutations p and q of length n. Find a permutation r, such that for every 1 <= i <= n, q[i] = p[r[i]].

Permutation of length n is an array consisting of distinct numbers from 1 to n in some order.

Example

Input:
p = [5, 1, 3],  q = [3, 1, 5]

Output:
r = [3, 2, 1]
[input] array.integer p

[input] array.integer q

[output] array.integer

permutation r
"""
# def findPermutation(p, q):
#     r = []
#     for i in q:
#         r.append(p.index(i) + 1)
#     return r
    
def findPermutation(p, q):
    r = [p.index(i) + 1 for i in q]
    return r

print(findPermutation([5,1,3], [3,1,5]))