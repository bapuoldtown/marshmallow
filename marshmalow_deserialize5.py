from marshmallow import *

class Inventory(object):
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity
    def __repr__(self):
        return "Class Created with attributes : {} {}".format(self.name,self.quantity)

    

class InventorySchema(Schema):
    name=fields.Str()
    quantity=fields.Float()


user_input1={'name':"A",'quantity':10}
user_input2={'name':"B",'quantity':20}

user_inputs=[user_input1,user_input2]

results=InventorySchema(many=True).load(user_inputs)

for row in results:
    print(row.__repr__())

pprint(results,indent=3)
    