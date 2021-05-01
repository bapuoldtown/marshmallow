import datetime as dt
from marshmallow import *
'''Demonstrate Nested Schemas'''
class User(object):
    def __init__(self,name,state,blogs):
        self.name=name
        self.state=state
        self.created_at=dt.datetime.now()
        self.blogs=blogs
        self.employer=None
class Blog(object):
    def __init__(self,title):
        self.title=title


'''Noe one Author can write multiple blogs'''

class BlogSchema(Schema):
    title=fields.Str()
    

class UserSchema(Schema):
    name=fields.Str()
    state=fields.Str()
    created_at=fields.DateTime()
    blogs=fields.Nested(BlogSchema,many=True)


blog1=Blog(title="Prison War")
blog2=Blog(title="Fort Delaware")
user=User(name="Veronica",state="Wyoming",blogs=[blog1])



result=UserSchema().dump(user)

pprint(result.get('blogs'),indent=2)
