from marshmallow import Schema,fields,pprint
from classmodels import User


class UserSchema(Schema):
    name=fields.Str()
    email=fields.Email()
    created_at=fields.DateTime()

'''Creates an instance of user and dump it'''
user=User(name="Guru",email="guru.pattnayak@gmail.com")
'''Create a schema object to dump it or serialize it'''
userschema=UserSchema()

result=userschema.dump(user)

'''Extract the serialised data below'''
#pprint(result)
#print(result)

'''Serilaze to a json string or dump into a json string'''

json_result=userschema.dumps(user)
#pprint(json_result)

'''Dump only selected fields'''
userschema=UserSchema(only=['name'])
json_result=userschema.dumps(user)
pprint(json_result)
