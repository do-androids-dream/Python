"""
Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
This class should contain method serialize for serialize object to filename according to  type. 
For defining format create enum FileType with values JSON, BYTE.
Create function serialize(object, filename, filetype).
This function use SerializeManager and should serialize object to filename according to type.
For example:
if user_dict = { 'name': 'Roman', 'id': 8}
then
serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file will contain user_dict as byte array
serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json" and text "String"
"""

import json
import pickle
from enum import Enum

class FileType(Enum):
    JSON = 1
    BYTE = 2

class SerializeManager:
    def __init__(self, filename, file_type):
        self.filename = filename
        self.file_type = file_type

    def __enter__(self):
        if self.file_type == FileType.JSON:
            self.file = open(self.filename, 'w')
        elif self.file_type == FileType.BYTE:
            self.file = open(self.filename, 'wb')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        
    def serialize(self, obj):
        if self.file_type == FileType.JSON:
            json.dump(obj, self.file)
        elif self.file_type == FileType.BYTE:
            pickle.dump(obj, self.file)

def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)
