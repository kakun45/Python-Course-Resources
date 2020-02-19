from marshmallow import Schema, fields, #INCLUDE, EXCLUDE --> this can be used to tell the laoder which fields are to be unsed and/or included


class BookSchema(Schema):
    title = fields.Str() # We can define which fields are require == fields.Str(requred=True)
    author = fields.Str() # We can define which fields are require == fields.Str(requred=True)
    description = fields.Str()
    
    
class Book:
    def __init__(self, title, author):
        a=self.title = title
        self.author = author
    

incoming_book_data = {
    "title": "The Pragmatic Programmer",
    "author": "Andy Hunt",
    "description": "One of the best books about software engineering."
    
}

book_schema = BookSchema() # in the argument we can use unknown=INCLUDE if we have imported the proper packages 
book = book_schema.load(incoming_book_data)
book_object = Book(**book)


print(book_object)
