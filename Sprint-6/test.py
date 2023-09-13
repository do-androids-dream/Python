# import json

# class Student:
#     def __init__(self, first_name: str, last_name: str):
#         self.first_name = first_name
#         self.last_name = last_name
    
#     @classmethod
#     def from_json(cls, data):
#         return cls(**data)
    
# class Team:
#     def __init__(self, students: []):
#         self.students = students

#     @classmethod
#     def from_json(cls, data):
#         students = list(map(Student.from_json, data["students"]))
#         return cls(students)
    
# student1 = Student(first_name="Jake", last_name="Foo")
# student2 = Student(first_name="Jason", last_name="Bar")
# team = Team(students=[student1, student2])

# print(list(map(lambda x: x.__dict__, team.students)))

# ### serialization
# data = json.dumps(
#     team, default=lambda o: o.__dict__, indent=4,
#     sort_keys=True)
# print(data)

# ### deserialization
# # print(**json.loads(data)["students"][0])
# decoded_team = Team.from_json(json.loads(data))
# print(decoded_team)
# print(decoded_team.students)


# d = {(1, 2, 3): "123", (4, 5, 6): "456", (7, 8, 9): "789"}
# print(*d)
# a = ["123", "456", "789"]
# print(**a)

person_info = {'name': 'John', 'age': 30, 'city': 'New York'}

# Use **dict to unpack the dictionary and pass it as keyword arguments
print(**person_info)