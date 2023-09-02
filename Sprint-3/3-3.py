"""
Create function create_account(user_name: string, password: string, secret_words: list). This function should return inner function check.

The function check compares the values of its arguments with password and secret_words: the password must match completely, secret_words may be misspelled (just one element).

Password should contain at least 6 symbols including one uppercase letter, one lowercase letter,  special character and one number.

Otherwise function create_account raises ValueError. 



For example: 

tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error 



If tom = create_account("Tom", "Qwerty1_", ["1", "word"])  

then 

tom("Qwerty1_",  ["1", "word"]) return True 

tom("Qwerty1_",  ["word"]) return False due to different length of   ["1", "word"] and  ["word"]

tom("Qwerty1_",  ["word", "12"]) return True

tom("Qwerty1!",  ["word", "1"]) return False because "Qwerty1!" not equals to "Qwerty1_"
"""
import re
def create_account(user_name, password, secret_words):
    if re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_])[a-zA-Z\d!@#$%^&*()_]{6,}$", password):
        def check(password2, secret_words2):
            count = 0
            secret_check = False
            if len(secret_words) == len(secret_words2):
                for i in secret_words:
                    if i in secret_words2:
                        count += 1
                        secret_words2.remove(i)
                if len(secret_words) - count <= 1:
                    secret_check = True
                if password == password2 and secret_check: check_result = True
                else: check_result = False
            else: check_result = False
            return check_result
    else:
        raise ValueError
    return check

tom = create_account("Tom", "Qwerty1_", ["1", "word"])
print(tom("Qwerty1_",  ["1", "word"])) #True
print(tom("Qwerty1_",  ["word"])) #False - len(list1) != len(list2)
print(tom("Qwerty1_",  ["word", "12"])) #True
print(tom("Qwerty1!",  ["word", "1"])) #False

user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
print(user2("yu6r*Tt5",["abc3", "abc3", "abc3"])) #False

user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
print(user2("yu6r*Tt5",["word1", "zzzz", "z"])) #False