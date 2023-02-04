from flask import Flask
application = app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World! - Running on Port 8002"

if __name__ == "__main__":
    app.run(),port=8003
