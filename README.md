# local_API_server
Python Script that would enable HTTP  methods(POST,GET,PUT and DELETE) using Flask library in a internal protocol.

## Dependencies
pip install flask,
pip install request

## Assigning http handler
@app. route("/") is a Python decorator that Flask provides to assign URLs in our app to functions easily. It's easy to understand what is happening at first glance: the decorator is telling our @app that whenever a user visits our app domain (myapp.com) at the given .

`@app.route('/ping')
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
    return jsonify({"message":"Product not found"})`

## Calling methods in flask
By default, the Flask route responds to GET requests.However, you can change this preference by providing method parameters for the route () decorator.
To handle both GET and POST requests, we add that in the decorator app.route() method.
Whatever request you want, you cahnge it in the decorator.

`@app.route('/products',methods=['POST'])
def addPoduct():
    new_product = {
            "Name": request.json['Name'],
            "price": request.json['price'],
            "quantity": request.json['quantity']                
            }
    products.append(new_product)
    return jsonify({"message":"Item was added succesfully","products":products})`


## Declare a local port for server
app.run(host='0.0.0.0', port=80) This would run the server in certain port set up.
