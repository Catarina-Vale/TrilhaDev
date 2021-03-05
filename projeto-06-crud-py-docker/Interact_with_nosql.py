from mongoengine import *
import json
connect(host='mongodb+srv://oiojoio:blabla89@repositories.d2klp.mongodb.net/CrudProject')

class User(Document):
    Name = StringField()
    Description = StringField()
    Value = FloatField()

def get_all_products():
    output = []
    cont = {}
    for entity in User.objects:
        cont = {"Name": entity.Name, "Desc": entity.Description, "Value": entity.Value}
        output.append(cont)
    return json.dumps(output)

def get_single_product(ProductName):
    find_them = User.objects(Name = ProductName).first()
    if find_them is not None:
        output = {"Name": find_them.Name, "Desc": find_them.Description, "Value": find_them.Value}
        return json.dumps(output)
    else:  
        return 'Product not registered'

def post_product(ProductName, Desc, Price):
    find_them = User.objects(Name = ProductName).first()
    if find_them is not None:
        return "Product already exists"
    else:
        newuser = User(Name = ProductName, Description = Desc, Value= float(Price)).save()
        return "Product successfully registered"

def put_product(ProductName, Desc, Price):
    find_them = User.objects(Name = ProductName).first()
    if Desc is None and Price is None:
        return "Need any new info to update"
    if find_them is not None:
        if Desc is not None:
            find_them.Description = Desc
        if Price is not None:
            find_them.Value = float(Price)
        find_them.save()
        return "Product updated with success"
    else:
        return "Product not found"

def delete_product(ProductName):
    find_them = User.objects(Name = ProductName).first()
    if find_them is not None:
        find_them.delete()
        return "Product deleted"
    else:
        return "Product not found"

