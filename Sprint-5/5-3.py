"""
Write the function sum_slice_array(arr, first, second), which accepts the array (list) arr and 
two numbers (first and second) - the ordinal numbers of the elements of the array that must be added. 
For example, if 3 and 5 were entered, the 3rd and 5th elements must be added.

The function should generate exceptions MyExceptions:
if non-numbers or numbers less than 1 were entered;
if non-numbers obtained from array;
if when one of the numbers or both is larger than the array length.
"""
class MyExceptions(Exception):
    def __init__(self):
        self.text = "MyExceptions"
    
    def __repr__(self):
        return self.text
    
def sum_slice_array(arr, first, second):
    try:
        if first < 1 or second < 1:
            raise MyExceptions
        return float(arr[first - 1] + arr[second - 1])
    except Exception:
        raise MyExceptions