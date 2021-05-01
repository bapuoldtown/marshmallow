from marshmallow import Schema,fields,ValidationError

'''Schema class for Item and use the validate parameter yto validate using an external function'''
item_data={'quantity':21}
def item_quantity(n):
    if n < 0:
        raise VaidationError('Quantity cannot be less than 0')
    if n >= 20:
        raise ValidationError('Quantity cannot be greater than 20')

class ItemSchema(Schema):
    quantity=fields.Integer(validate=item_quantity)

try:
    itemschema=ItemSchema().load(item_data)
except ValidationError as err:
    print(err.messages)

