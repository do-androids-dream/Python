"""
Class Student has attributes full_name:str, avg_rank: float, courses: list
Class Group has attributes title: str, students: list.

Make both classes JSON serializable. 

Json-files represent information about student (students). 

Create methods:  

Student.from_json(json_file) that return Student instance from attributes from json-file;

Student.serialize_to_json(filename)

Group.serialize_to_json(list_of_groups, filename)

Group.create_group_from_file(students_file)

Parse given files, create instances of Student class and create instances of Group class (title for group is name of json-file without extension).
"""
import json
from json import JSONEncoder

class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    @classmethod
    def from_json(cls, json_file):
        with open(json_file, "r") as file:
            data = json.load(file)
            if type(data) is dict:
                return cls(**data)
            elif type(data) is list:
                students = [cls(**item) for item in data]
                return students
       
    def serialize_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.__dict__, json_file)

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students
    
    @classmethod
    def serialize_to_json(cls, list_of_groups, filename):
        data = [{'title': group.title, 'students': [student.__dict__ for student in group.students]} for group in list_of_groups]
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)

    @classmethod
    def create_group_from_file(cls, students_file):
        title = students_file.split('.')[0]
        students = Student.from_json(students_file)
        return cls(title, students)

std1 = Student("Victor", 5.5, ["C++", "Python"])
user1 = Student.from_json("test.json")
print(user1)