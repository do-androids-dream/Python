"""
In user.json file we have information about users in format [{“id”: 1, “name”: “userName”, “department_id”: 1}, ...], 

in file department.json are information about departments in format: [{“id”: 1, “name”: “departmentName”}, ...]. 

Function user_with_department(csv_file, user_json, department_json) should read from json files information and create csv file in format:

header line - name, department

next lines :  <userName>, <departmentName>

If file department.json doesn't contain department with department_id from user.json we generate DepartmentName exception.

Create appropriate json-schemas for user and department.

If schema for user or department doesn't satisfy formats described above we should generate InvalidInstanceError exception  

To validate instances create function validate_json(data, schema)
"""
import json
import csv
from jsonschema.validators import validate

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "department_id": {"type": "integer"},
    },
    "required": ["id", "name", "department_id"],
}

department_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
    },
    "required": ["id", "name"],
}

def validate_json(data, schema):
    try:
        validate(data, schema)
    except Exception as e:
        raise InvalidInstanceError("Error in user schema")

class DepartmentName(Exception):
    pass

class InvalidInstanceError(Exception):
    pass

def user_with_department(csv_file, user_json, department_json):
    with open(user_json, 'r') as user:
        with open(department_json, 'r') as dep_t:
            user_data = json.load(user)
            dep_data = json.load(dep_t)
            try:
                dep_id_name = {dep["id"]: dep["name"] for dep in dep_data}
            except Exception as e:
                raise InvalidInstanceError("Error in department schema")
            with open(csv_file, 'w', newline='') as output:
                header = ["name", "department"]
                writer = csv.DictWriter(output, fieldnames=header)
                writer.writeheader()
                for user in user_data:
                    validate_json(user, user_schema)
                    if user['department_id'] not in dep_id_name:
                        raise DepartmentName(f"Department with id {user['department_id']} not found")
                    
                    writer.writerow({'name': user['name'], 'department': dep_id_name[user["department_id"]]})

user_with_department("output.csv", "user.json", "department.json")
