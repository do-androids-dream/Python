"""
Please specify a regular expression for matching publication formats such as "Head First. Python: PROSystem, 2021 and "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022
"""
import re

def pretty_message(data):
    pattern = "(.*\d{4})(\s.*\d{4})"
    return list((re.findall(pattern, data))[0])

data = "Head First. Python: PROSystem, 2021 and Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022"
print(pretty_message(data))
# ['Head First. Python: PROSystem, 2021', ' and Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022']
