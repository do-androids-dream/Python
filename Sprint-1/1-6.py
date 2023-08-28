"""
Write a program that given an array of integers determines if it is sorted in "ascending" order, "descending" order or "not sorted" at all.

Example

For a = [10, 5, 4], the output should be
order(a) = "descending";
For a = [6, 20, 160, 420], the output should be
order(a) = "ascending";
For a = [1, 7, 0, 4, 8, 1], the output should be
order(a) = "not sorted".
[input] array.integer a

1 < a.length < 100, all of numbers are different

[output] string

"ascending", "descending" or "not sorted".
"""
def order(a):
    str = ""
    for i in range(1, len(a)):
        if a[i] > a[i-1] and str != "descending": str = "ascending"
        elif a[i] < a[i-1] and str != "ascending": str = "descending"
        else: return "not sorted"
    return str

print(order([10, 5, 4]))