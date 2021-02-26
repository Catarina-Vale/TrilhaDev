
import Interact_with_nosql
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def helloworld():
    print('user accessed mainpage')
    return "<h1>Welcome to the main page</h1>"

@app.route("/products", methods = ['GET', 'POST', 'DELETE', 'PUT'])
def mainfunction():
    if request.method == 'GET':
        print('user requested all products')
        return Interact_with_nosql.get_all_products()
    elif request.method == 'POST':
        ProductName = request.form.get('Name')
        ProductDesc = request.form.get('Desc')
        ProductValue = request.form.get('Value')
        if ProductName is None:
            return '<h1>Name is required</h1>'
        print(f'user wants to post product {ProductName}:\n{ProductDesc}\n{ProductValue}')
        return Interact_with_nosql.post_product(ProductName, ProductDesc, ProductValue)
    elif request.method == 'PUT':
        ProductName = request.args.get('Name')
        ProductDesc = request.args.get('Desc')
        ProductValue = request.args.get('Value')
        if ProductName is None:
            return '<h1>Name is required</h1>'
        print(f'user wants to update product {ProductName}:\n{ProductDesc}\n{ProductValue}')
        return Interact_with_nosql.put_product(ProductName, ProductDesc, ProductValue)
    elif request.method == 'DELETE':
        ProductName = request.args.get('Name')
        print(f'user wants to delete product {ProductName}')
        return Interact_with_nosql.delete_product(ProductName)

@app.route("/products/<string:product>", methods = ['GET', 'DELETE'])
def individualfunction(product):
    if request.method == 'GET':
        print(f'user requested product: {product}')
        return Interact_with_nosql.get_single_product(product)

    elif request.method == 'DELETE':
        print(f'user wants to delete product {product}')
        return Interact_with_nosql.delete_product(product)
if __name__ == '__main__':
    print('listening in port 5000...')
    app.run(host='0.0.0.0',port=5000)
    print('Shut down')