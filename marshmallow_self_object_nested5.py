'''Here we neste varuous user objects inside a user object so the same object is nesting multiple objects which are its siblings pointing ti the same user class called User'''
from marshmallow import *

class User(object):
    def __init__(self,name,state,friends=[]):
        self.name=name
        self.state=state
        self.friends=friends

class UserSchema(Schema):
    name=fields.String()
    state=fields.String()
    friends=fields.Nested('self',many=True,default=[],only=('name','state'),order_by=('state'))




u2=User('Uddipan',state='Dellaware')
u3=User('Lokesh',state='Florida')
ulist=[u2,u3]
u1=User('Guru',state='Wisconsin',friends=ulist)

u2.friends.extend([u1,u3])

results=UserSchema().dump(u2)

pprint(results,indent=4)


