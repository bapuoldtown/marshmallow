'''Objective is to populate a field in the serulaizer calss from a actual field in the model class by refining them in certain Methods in the serilaizer class itself'''
'''The method of the serializer class takes self and the obj and the obj access the field names of the model classes'''


from marshmallow import *
class User(object):
    def __init__(self,name=None,state=None):
        self.name=name
        self.state=state

class UserSchema(Schema):
    name=fields.Str()
    state=fields.Str()
    titlename=fields.Method("title_name")

    def title_name(self,obj):
        if obj.name is None:
            return 'No name specified heyy bawa'
        return obj.name.title()

u1=User(state="Washington")

result=UserSchema().dump(u1)

pprint(result)