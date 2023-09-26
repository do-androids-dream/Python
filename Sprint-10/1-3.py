"""
Declarative mapping
"""
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///library-2.db', echo=True)
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
    

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship(Author, backref=backref('books', order_by=title))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return f"{self.id} Title:{self.title} by {self.author}"
    
Base.metadata.create_all(engine) # DB tables creation

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine) #connection to DB
session = Session()

author_1 = Author('Richard Dawkins')
author_2 = Author('Matt Ridley')
book_1 = Book('The Red Queen', 'A popular science book', author_2)
book_2 = Book('The Selfish Gene', 'A popular science book', author_1)
book_3 = Book('The Blind Watchmaker', 'The theory of evolution', author_1)

session.add(author_1)
session.add(author_2)
session.add(book_1)
session.add(book_2)
session.add(book_3)
# session.add_all([author_1, author_2, book_1, book_2, book_3]) # all at once
# book_3 in session # check whether the object is in the session
session.commit() # make changes to DB

book_3.description = 'The Theory Of Evolution' # update the object
session.commit() # make changes to DB

session.query(Book).order_by(Book.id) # returns a query
session.query(Book).order_by(Book.id).all() # returns an object-list
session.query(Book).filter(Book.title == 'The Selfish Gene').order_by(Book.id).all()
session.query(Book).filter(Book.title.like('The%')).order_by(Book.id).all()

query = session.query(Book).filter(Book.id == 9).order_by(Book.id)
query.count() # returns 0L
query.all() # returns an empty list
query.first() # returns None
query.one() # raises NoResultFound exception

query = session.query(Book).filter(Book.id == 1).order_by(Book.id)
book_1 = query.one()
book_1.description # returns u'A popular science book'
book_1.author.books # returns a list of Book-objects representing all the books from the same author.

# get a list of all Book-instances where the author's name is 'Richard Dawkins'
session.query(Book).filter(Book.author_id==Author.id).filter(Author.name=='Richard Dawkins').all()
session.query(Book).join(Author).filter(Author.name=='Richard Dawkins').all()
session.query(Book).\
    from_statement('SELECT b.* FROM books b, authors a WHERE b.author_id = a.id AND a.name=:name').\
    params(name='Richard Dawkins').all()