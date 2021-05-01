from  collections import OrderedDict
from marshmallow import *
import datetime as dt
def default_time():
    return dt.datetime.now()

class User(object):
    def __init__(self,name,email):
        self.name=name
        self.email=email
       
      

class UserSchema(Schema):
    uppername = fields.Function(lambda obj: obj.name.upper())
    created_at= fields.Function(default_time())

    class Meta:
        fields = ("name", "email", "created_at", "uppername")
        ordered = True

u = User('Charlie', 'charlie@stones.com')
schema = UserSchema()
result = schema.dump(u)

# marshmallow's pprint function maintains order 
pprint(result, indent=2)

