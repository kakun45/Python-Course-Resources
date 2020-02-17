from marshmallow import Schema, fields


class BookSchema(Schema):
    # This is going to define what fields are in a book class
    
    title = fields.Str()
    author = fields.Str()
    

class Book:
    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description
        

book = Book("The Pragmatic Programmer", "Andy Hunt", "One of the best books about software engineering.")

book_schema = BookSchema()
book_dict = book_schema.dump(book)

print(book_dict)