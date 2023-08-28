"""
's3ooOOooDy' has exams. He wants to study hard this time. He has an array of studying hours per day for the previous exams. He wants to know the length of the maximum non-decreasing contiguous subarray of the studying days, 
to study as much before his current exams.

Example:

For a = [2,2,1,3,4,1] the answer is 3.

[input] array.integer a

The number of hours he studied each day.

[output] integer

The length of the maximum non-decreasing contiguous subarray.
"""
def studying_hours(a):
    count = 0
    non_dec = 0
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            count = 0
        if a[i] >= a[i-1]: 
            count += 1
            if non_dec <= count: non_dec = count
    return non_dec + 1

print(studying_hours([2,2,1,3,4,1]))