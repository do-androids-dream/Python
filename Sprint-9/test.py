USERS_LIST = [
                {
                    "id": 1,
                    "username": "theUser",
                    "firstName": "John",
                    "lastName": "James",
                    "email": "john@email.com",
                    "password": "12345",
                }
            ]

# path = "/user/theUser"
# data = None
# username = path[6:]
# for user in USERS_LIST:
#     if user["username"] == username:
#         data = user
#         print(data)
#         break

# data_2 = [3, 4]
# data = {1: "abc", 2: "def", 3: "ghj", 4: "jkl"}

# res = [el in data for el in data_2]
# print(res)
data = {1: "abc", 2: "def", 3: "ghj", 4: "jkl"}
data2 = [{1: "abc", 2: "def", 3: "ghj", 4: "jkl"}, {11: "abc", 22: "def", 33: "ghj", 44: "jkl"}]

USERS_LIST.extend(data)
print(USERS_LIST)