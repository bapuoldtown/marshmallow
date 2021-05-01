from marshmallow import Schema,fields,ValidationError

class UserSchema(Schema):
    name=fields.String(required=True)
    state=fields.String(required=True,attribute='state1')
'''
try:
    UserSchema().load({'state':'Wisconsin'},partial=('name',))
except ValidationError as err:
    print(err.messages)
'''
errors=UserSchema().validate({'state1':'Wisconsin'})
print(errors)
