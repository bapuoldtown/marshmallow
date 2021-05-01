'''In the Method and Function fields we use one optional argument called as deserialize'''
from marshmallow import *

class User(object):
    def __init__(self,name=None,income=None,debt=None):
        self.name=name
        self.income=income
        self.debt=debt
    
class UserSchema(Schema):

    getbalance=fields.Method('get_balance')
    income=fields.Method(deserialize='get_income')
    def get_balance(self,obj):
        return obj.income-obj.debt
    
    def load_balance(self,value):
        return float(value)
    
    def get_income(self,value):
        return float(value)
    class Meta:
        fields=('name','income','getbalance')

u1=User(name="Guru",income=1000,debt=100)


results=UserSchema().dump(u1)

'''Deserialize the values to Objects of User Class'''
input_dict={'name':"Uddipan",'income':'300.00'}
results_desrialize=UserSchema().load(input_dict)



pprint(results)
print(results_desrialize)