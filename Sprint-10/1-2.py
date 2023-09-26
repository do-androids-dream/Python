"""
Create a Python program to use the sqlite database named "q1.db". The query to the database should display information, as shown in the example below, including phrases: about the successful connection, the total number of records, the actual records, the record of closing the database. From the table of "customers" to deduce all records for which in a "grade" field of value more than 200 with sort ordering on id



For example output:

Connected to SQLite
Total rows are:   2
Printing each row
Id:  3022
Name:  Nik Rimando
City:  Madrid
Grade:  1000
Seller:  6001


Id:  3025
Name:  Grem Zusisa
City:  USA
Grade:  2000
Seller:  6002


The SQLite connection is closed
"""


import sqlite3

conn = sqlite3.connect('q1.db')
print("Connected to SQLite")
ptr = conn.cursor()

ptr.execute("select * from customers where grade > 200 order by id")
result = ptr.fetchall()
print(f"Total rows are:   {len(result)}")
print("Printing each row")
print(f"Id:  {result[0][0]}", f"Name:  {result[0][1]}", f"City:  {result[0][2]}", f"Grade:  {result[0][3]}", f"Seller:  {result[0][4]}\n\n", sep='\n')
print(f"Id:  {result[1][0]}", f"Name:  {result[1][1]}", f"City:  {result[1][2]}", f"Grade:  {result[1][3]}", f"Seller:  {result[1][4]}\n\n", sep='\n')
conn.close()
print("The SQLite connection is closed")