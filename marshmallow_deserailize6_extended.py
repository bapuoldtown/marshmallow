from marshmallow_deserailize6 import AuthorSchema,BookSchema
from classModelsRecursion import *
from marshmallow import *



agatha=Author(name="Agatha Christie",country="England")
book1=Book(name="the Dumb Witness",author=agatha,genre="Crime Fiction")
book2=Book(name="Mysterious Affair at Styles",author=agatha,genre="Crime Fiction")
books=[book1,book2]

result = BookSchema(many=True).dump(books)
pprint(result)