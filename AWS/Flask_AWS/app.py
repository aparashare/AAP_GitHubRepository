# Ref: https://flask.palletsprojects.com/en/2.1.x/quickstart/ 
# First we imported the Flask class. An instance of this class will be our WSGI application.
#from flask import Flask                 

# Next we create an instance of this class. Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)

# We then use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')

# The function returns the message we want to display in the user’s browser. 
def hello_world():
    return "Hello World - Flask App"

#if __name__ == "__main__":
#    app.run(host="0.0.0.0, port = 5000", debug=True)