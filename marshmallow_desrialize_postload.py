from marshmallow import Schema,fields,pprint,post_load
from marshmallow.exceptions import ValidationError
from classmodels import User
import datetime as dt


'''Seriakizer schema class'''
class UserSchema(Schema):
    name=fields.Str()
    email=fields.Email()
    created_at=fields.DateTime()
  


'''Create a dictionary and deserialize it and then create a user instance using the postload decorator'''
user_data = {'name': 'Ken','email': 'guru@example.com'}

userschema=UserSchema()
data,errors=UserSchema().load(user_data)

print(data)
print(errors)


