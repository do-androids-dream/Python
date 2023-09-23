import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from jsonschema.validators import validate

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


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}, indent=4).encode('utf-8'))

    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        return json.loads(self.rfile.read(content_length).decode('utf-8'))  # <--- Gets the data itself

    def do_GET(self):
        global USERS_LIST
        if self.path == "/reset":
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
            self._set_response(200, {"info": "You are lucky - DONE"})
        elif self.path == "/users":
            self._set_response(200, USERS_LIST)
        elif self.path.startswith("/user/"):
            user_name = self.path[6:]
            print(user_name)
            data = None
            for user in USERS_LIST:
                if user["username"] == user_name:
                    data = user
                    break
            if data:
                self._set_response(200, data)
            else:
                self._set_response(400, {"error": "User not found"})
        else:
            self._set_response(418)

    def do_POST(self):
        global USERS_LIST
        self.request = self._pars_body()
        self.structure = {
            "type": "object",
            "properties": {
            "id": {"type": "number"},
            "username": {"type": "string"},
            "firstName": {"type": "string"},
            "lastName": {"type": "string"},
            "email": {"type": "string"},
            "password": {"type": "string"},
             },
            "required": [
                "username", 
                "firstName", 
                "lastName", 
                "email", 
                "password"
                ]
        }

        def struct_validation():
            if isinstance(self.request, list):
                for obj in self.request:
                    try:
                        validate(obj, self.structure)
                    except Exception:
                        return False
                    else:
                        return True
            elif isinstance(self.request, dict):
                try:
                    validate(self.request, self.structure)
                except Exception:
                    return False
                else:
                    return True
                
        if struct_validation():
            status = 1
            if self.path == "/user":
                if isinstance(self.request, dict):
                    for user in USERS_LIST:
                        if user["id"] == self.request["id"]:
                            self._set_response(400)
                            status = 0
                    if status:
                        USERS_LIST.append(self.request)
                        self._set_response(201, self.request)
            elif self.path == "/user/createWithList":
                if isinstance(self.request, list):
                    for user in USERS_LIST:
                        for new_users in self.request:
                            if user["id"] == new_users["id"]:
                                self._set_response(400)
                                status = 0
                    if status:
                        USERS_LIST.extend(self.request)
                        self._set_response(201, self.request)
        else:
            self._set_response(400)
        
    def do_PUT(self):
        global USERS_LIST
        self.request = self._pars_body()
        self.structure = {
            "type": "object",
            "properties": {
            "username": {"type": "string"},
            "firstName": {"type": "string"},
            "lastName": {"type": "string"},
            "email": {"type": "string"},
            "password": {"type": "string"},
             },
            "required": [
                "username", 
                "firstName", 
                "lastName", 
                "email", 
                "password"
                ]
        }

        def struct_validation():
            if isinstance(self.request, dict):
                try:
                    validate(self.request, self.structure)
                except Exception:
                    return False
                else:
                    return True
                
        if struct_validation():
            status = 1
            ind = 0
            if self.path.startswith("/user/"):
                id = int(self.path[6:])
                for user in USERS_LIST:
                    if user["id"] == id:
                        USERS_LIST[ind]["id"] = id
                        USERS_LIST[ind]["username"] = self.request["username"]
                        USERS_LIST[ind]["firstName"] = self.request["firstName"]
                        USERS_LIST[ind]["lastName"] = self.request["lastName"]
                        USERS_LIST[ind]["email"] = self.request["email"]
                        USERS_LIST[ind]["password"] = self.request["password"]
                        self._set_response(200, user)
                        status = 0
                        break
                    ind += 1
                if status:
                    self._set_response(404, {"error": "User not found"})
        else:
            self._set_response(400, {"error": "not valid request data"})

    def do_DELETE(self):
        if self.path.startswith("/user/"):
            id = int(self.path[6:])
            ind = 0
            status = 1
            for user in USERS_LIST:
                if user["id"] == id:
                    USERS_LIST.pop(ind)
                    self._set_response(200)
                    status = 0
                    break
            if status:
                self._set_response(404, {"error": "User not found"})
    

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()