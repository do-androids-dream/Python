"""
Given a string, check if its characters can be rearranged to form a palindrome. Where a palindrome is a string that reads the same left-to-right and right-to-left.

Example

"trueistrue" -> false;
"abcab" -> true because "abcba" is a palindrome
[input] string s (min 1 letters) 

[output] boolean
"""
def isPalindrome(str):
    if str == str[::-1]:
        return True
    count = 0
    for i in str:
        if str.count(i) % 2 != 0:
            count += 1
            if count > 1:
                return False
    return True

print(isPalindrome("t"))