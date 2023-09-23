from flask import Flask

app = Flask(__name__)


# this decorator registers function index() 
# as the handler for the app root URL
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

# Dynamic route
@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello, {name}!</h1>"
