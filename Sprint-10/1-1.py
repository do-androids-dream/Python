# import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('sqlite:///library.db', echo=True)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text

metadata = MetaData()

authors_table = Table('authors',
                      metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String))
books_table = Table('books',
                    metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String),
                    Column('description', String),
                    Column('author_id', ForeignKey('authors.id')))

metadata.create_all(engine) # creates the tables

# INSERT INTO authors (id, name) VALUES (:id, :name)
insert_stmt = authors_table.insert().values(name='Alexandre Dumas') # insert single entry)
conn = engine.connect() #open connection
conn.execute(insert_stmt)
conn.close()

conn = engine.connect()
conn.execute(authors_table.insert(), [{'name': 'Mark Twen'}, {'name': 'Mr X'}]) # a list of entries
conn.close()

# SELECT
select_stmt = authors_table.select().where(authors_table.c.id==2)
conn = engine.connect()
result = conn.execute(select_stmt)
print(result.fetchall())
print(result)
conn.close()

# DELETE
del_stmt = authors_table.delete().where(text("name='Mr X'"))
conn = engine.connect()
conn.execute(del_stmt)
conn.close()

del_all_stmt = authors_table.delete() # delete all
conn = engine.connect()
conn.execute(del_all_stmt)
conn.close()