from flask import Flask
app = application = Flask(__name__)

@app.route('/')

def index():
    return 'Welcome to flask app'

if __name__ == "__main__":
   application.run()
#   application.run(debug=True,port=3000)