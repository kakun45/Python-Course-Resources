from marshmallow import Schema, fields, #INCLUDE, EXCLUDE


class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()
    description = fields.Str()
    
    
class Book:
    def __init__(self, title, author):
        a=self.title = title
        self.author = author
    

incoming_book_data = {
    "title": "The Pragmatic Programmer",
    "author": "Andy Hunt",
    "description": "AOne of the best books about software engineering."
    
}

book_schema = BookSchema()
book = book_schema.load(incoming_book_data)
book_object = Book(**book)


print(book_object)
