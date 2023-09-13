"""
Implement function parse_user(output_file, *input_files) for creating file that will contain only unique records (unique by key "name") 
by merging information from all input_files argument (if we find user with already existing name from previous file we should ignore it). 
Use pretty printing for writing users to json-file.


If the function cannot find input files we need to log information with error level  

root - ERROR - File <file name> doesn't exist

For example:
user1.json : 
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
]

user2.json : 
[{"name": "Bob1", "rate": 25, “languages": ["French"]},
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]

If we execute parse_user(user3.json, user1.json, user2.json)
then file user3.json should contain information:
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]
"""
import json
import logging

logging.basicConfig(filename="app.log", filemode="w", format="%(name)s - %(levelname)s - %(message)s", level="ERROR")

def parse_user(output_file, *input_files):
    names = []
    unique_data = []
    for i in input_files:
        try:
            with open(i, 'r') as temp:
                data = json.load(temp)
                for name in data:
                    if name["name"] not in names:
                        names.append(name["name"])
                        unique_data.append(name)
        except FileNotFoundError:
            logging.error(f"File {i} doesn't exist")
        except KeyError:
            unique_data = []
    with open(output_file, 'w') as output:
        json.dump(unique_data, output, indent=4)

parse_user("user3.json", "user1.json", "user2.json")