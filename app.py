# -*- coding: utf-8 -*-

from flask import Flask, jsonify,request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message":"Pong"})
@app.route('/products')
def getproducts():
    return jsonify({"products": products,"message": "Product's list"})
@app.route('/products/<string:product_name>')
def getproduct(product_name):
    productsFound = [product for product in products if product['Name']==product_name]
    if (len(productsFound) > 0):
        return jsonify({"product":productsFound[0]})
    return jsonify({"message":"Product not found"})

@app.route('/products',methods=['POST'])
def addPoduct():
    new_product = {
            "Name": request.json['Name'],
            "price": request.json['price'],
            "quantity": request.json['quantity']                
            }
    products.append(new_product)

    return jsonify({"message":"Item was added succesfully","products":products})

@app.route('/products/<string:product_name>',methods = ['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['Name']== product_name]
    if (len(productFound)>0):
        productFound[0]['Name'] = request.json['Name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({"message":"Product Updated",
                        "product":productFound[0]})
    return jsonify({"message":"Item not found"})


@app.route('/products/<string:product_name>',methods=['DELETE'])
def deleteproduct(product_name):
    productFound = [product for product in products if product['Name']== product_name]
    if len(productFound) > 0:
        products.remove(productFound[0])
        return jsonify({"message":"Product removed", 
                        "Products":products})
    return jsonify({"message":"Product was not found"})

if __name__=='__main__':
    app.run(debug=True,port=5000)

