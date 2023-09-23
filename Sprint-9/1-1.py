"""
1. Clone repo.

2. Install all requirement modules (pip install -r requirements.txt)

3. Implements tasks.

4. Run tests (python -m unittest tests.py).

5. Submit your commits to branch main.



UPDATE DO_GET METHOD:
if url /reset reset list USERS_LIST to

[   
    {
     "id": 1,
     "username": "theUser",
     "firstName": "John",
     "lastName": "James",
     "email": "john@email.com",
     "password": "12345",
    }
]

            
if url /users returns a json response that contains all users

if url /user/{username} returns a json response that contains all the user data with the corresponding username, if such a user does not exist then return the status code 400 and json

{
     "error": "User not found"
}
UPDATE DO_POST METHOD:
the request body is valid if it has such a structure

{
         "id": int,
         "username": str,
         "firstName": str,
         "lastName": str,
         "email": str,
         "password": str
}
or

 [
         {
             "id": int,
             "username": str,
             "firstName": str,
             "lastName": str,
             "email": str,
             "password": str
         },
         ...
 ] 
if body not valid return status code 400 and empty json

if url /user add user to list USERS_LIST and return status code 201 and this user, if id already exists then return status code 400 and empty json

if url /user/createWithList add users to list USERS_LIST and return status code 201 and these users, if at least some id already exists then return status code 400 and empty json

UPDATE DO_PUT METHOD:
the request body is valid if it has such a structure

{
  "username": str,
  "firstName": str,
  "lastName": str,
  "email": str,
  "password": str
}
if url /user/{id}

if update user in list USERS_LIST and return status code 200 and this user
if request data not valid return status code 400 and json
{
  "error": "not valid request data"
}
if id not already exists return status code 404 and json
{
  "error": "User not found"
}
UPDATE DO_DELETE METHOD:
if url /user/{id} return status code 200 and empty json else status code 404 and json
{
  "error": "User not found"
}


"""