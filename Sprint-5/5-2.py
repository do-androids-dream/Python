"""
Write the function valid_email(...) to check if the input string is a valid email address or not.

An email is a string (a subset of ASCII characters) separated into two parts by @ symbol, 
a “user_info” and a domain_info, that is personal_info@domain_info:
in case of correct email the function should be displayed the corresponding message – "Email is valid"
in case of incorrect email the function should be displayed the corresponding message – "Email is not valid"

Note: in the function you must use the "try except" construct.  
"""
import re

def valid_email(string):
    pattern = r"^\w+@([a-z]+\.)*[a-z]{2,3}$"
    try:
        re.match(pattern, string).group()
        return "Email is valid"
    except:
        return "Email is not valid"

print(valid_email("trafik@ukr.tel.com")) #Email is valid
print(valid_email("trafik@ukr_tel.com")) #Email is not valid
print(valid_email("ownsite@our.c0m")) #Email is not valid
print(valid_email("tra@fik@ukr.com")) #Email is not valid