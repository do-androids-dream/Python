"""
Create function find(file, key)
This function parses json-file and returns all unique values of the key.

1.json:
[{"name": "user_1”, "password": "pass_1”},
{"name": "user_2”, "password": ["pass_1", "qwerty“]} ]
find("1.json", "password") returns ["pass_1", "qwerty"]

2.json:
[{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}}, {"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]
find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]

3.json:
{"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}
find("3.json", "password") returns ["1234qweQWE"]
"""

import json

def find(file, key):
    with open(file, 'r') as temp:
        data = json.load(temp)
            
    def key_val(obj, key):
        if type(obj) is list:
            val = []
            for i in obj:
                val.extend(key_val(i, key))
            return val
        elif type(obj) is dict:
            val = []
            if key in obj:
                if type(obj[key]) is str:
                    val.append(obj[key])
                else: 
                    val.extend(obj[key])
            for i in obj.values():
                if type(i) is dict or type(i) is list:
                    val.extend(key_val(i, key))
            return val
        else: return []
    
    val = list(set((key_val(data, key))))
    return val

print(find("2.json", "password"))