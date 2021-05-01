
from marshmallow import *
'''Demonstrates a Recursive Nested Relation Ship'''


class BookSchema(Schema):
    class Meta:
        fields=('bookname','author','genre')
class AuthorSchema(Schema):
    class Meta:
        fields=('authorname','country')




