from marshmallow import *
from marshmallow.exceptions import *

class BandMember(object):
    def __init__(self,name=None,email=None):
        self.name=name
        self.email=email
    

class BandMemberSchema(Schema):
    name=fields.String(required=True)
    email=fields.Email()

user_datas=[{'name':'Guru','email':'guru@example.com'},{'name':'Bapu','email':'bapu@example.com'},{'email':'winnie@example.com'}]


data,errors=BandMemberSchema(many=True).load(user_datas)

print(errors)


