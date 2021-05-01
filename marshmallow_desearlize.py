from marshmallow import Schema,fields,pprint
from marshmallow.exceptions import ValidationError

'''Seriakizer schema class'''
class UserSchema(Schema):
    name=fields.Str()
    email=fields.Email()
    created_at=fields.DateTime()

'''Create a dictionary and deserialize it'''
user_data = {
'email': u'guru@example.com','name': u'Ken'}


try:
    userschema=UserSchema()
    result_json=userschema.load(user_data)
    pprint(result_json.data)
except ValidationError:
    pprint("Error Michael in Validation to concert dictionary to object istance")

