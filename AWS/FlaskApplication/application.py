from flask import Flask
application = app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World! - Abhijit Parashare"

if __name__ == "__main__":
    app.run()