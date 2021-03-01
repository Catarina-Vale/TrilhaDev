from mongoengine import *
from flask import Response
connect(host='mongodb+srv://oiojoio:blabla89@repositories.d2klp.mongodb.net/CrudProject')

class User(Document):
    Name = StringField()
    Description = StringField()
    Value = FloatField()

def get_all_products():
    output = '<h1>Todos os produtos:</h1>'
    for entity in User.objects:
        output += f'<h2>{entity.Name}</h2> <p>Descrição: {entity.Description}</p> <p>Preço: {entity.Value}</p>'
    return output

def get_single_product(ProductName):
    find_them = User.objects(Name = ProductName).first()
    if find_them is not None:
        header = f'<h1>{find_them.Name}</h1>'
        body = f'<p>Descrição: {find_them.Description}</p> <p>Preço: {find_them.Value}</p>'
        whole = header + body
        return whole
    else:
        return Response('<h1>Product isnt resgistered</h1>',status=404)

def post_product(ProductName, Desc, Price):
    find_them = User.objects(Name = ProductName).first()
    if find_them is not None:
        return Response('<h1>Product already registered</h1>',status=400)
    else:
        newuser = User(Name = ProductName, Description = Desc, Value= float(Price)).save()
        return Response('<h1>Product successfully registered</h1>', status=200)

def put_product(ProductName, Desc, Price):
    find_them = User.objects(Name = ProductName).first()
    if Desc is None and Price is None:
        return Response('<h1>Need new info to update</h1>',status=400)
    if find_them is not None:
        if Desc is not None:
            find_them.Description = Desc
        if Price is not None:
            find_them.Value = float(Price)
        find_them.save()
        return Response('<h1>Product successfully updated</h1>',status=200)
    else:
        return Response('<h1>Product not found</h1>',status=404)

def delete_product(ProductName):
    find_them = User.objects(Name = ProductName).first()
    if find_them is not None:
        find_them.delete()
        return Response('<h1>Product successfully deleted</h1>',status=200)
    else:
        return Response('<h1>Product not found</h1>',status=404)

