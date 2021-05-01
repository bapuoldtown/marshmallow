'''Objective is to populate the fiels after serialization by using a different fields class
Please note thus field class will be derived from fields.Field respectively'''
from marshmallow  import *



class TitleCased(fields.Field):
    def _serilaize(self,value,attr,obj):
        if value is None:
            return ''
        return attr.title()

class User(object):
    def __init__(self,name,state):
        self.name=name
        self.state=state

class UserSchema(Schema):
    name=fields.Str()
    state=fields.Str()
    titlename=TitleCased(attr='name')

u1=User(name="paul",state="Nort Dakota")

result=UserSchema().dump(u1)
pprint(result)




