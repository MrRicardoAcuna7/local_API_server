# local_API_server
Python Script that would enable HTTP  methods(POST,GET,PUT and DELETE) using Flask library in a internal protocol.

##Dependencies
pip install flask,
pip install request

##Assigning hhtp handler
@app. route("/") is a Python decorator that Flask provides to assign URLs in our app to functions easily. It's easy to understand what is happening at first glance: the decorator is telling our @app that whenever a user visits our app domain (myapp.com) at the given .

##Calling methods in flask
By default, the Flask route responds to GET requests.However, you can change this preference by providing method parameters for the route () decorator.
To handle both GET and POST requests, we add that in the decorator app.route() method.
Whatever request you want, you cahnge it in the decorator.

##Declare a local port for server
app.run(host='0.0.0.0', port=80) This would run the server in certain port set up.
