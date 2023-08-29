"""
How would you find a word or words that end in 4 lowercase letters and have at least one zero in front of them?

Write a regular expression.

For example, in line "0msdfgh 00000xbcd 0bbcd7 hjkj00wjhg hjkj0ajhg" this pattern matches the words "00000xbcd", "hjkj00wjhg", "hjkj0ajhg".
"""
import re

# def pretty_message(data):
#     pattern = r"\b(\w*0[a-z]{4})\b"
#     return re.findall(pattern, data)

def pretty_message(data):
    string = ""
    pattern = r"\b(0?[a-z1-9]+)"
    result = re.findall(pattern, data)
    print(result)
    return " ".join(result)

data = "0msdfgh 00000xbcd 0bbcd7 hjkj00wjhg hjkj0ajhg"
print(pretty_message(data))
# 0msdfgh  0bbcd7 hjkj hjkj