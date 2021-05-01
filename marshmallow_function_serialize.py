'''Objective is to use a function which will be defined in line with the serilaizer class attributes using a simple lambda '''

from marshmallow import *
class User(object):
    def __init__(self,name,state):
        self.name=name
        self.state=state

class UserSchema(Schema):
    name=fields.Str()
    state=fields.Str()
    uppername=fields.Function(lambda a:a.name.upper())

u1=User(name="guru",state="Kentucky")

result=UserSchema().dump(u1)
pprint(result)