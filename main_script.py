'__author__' == 'cyril'


from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello from the other side"
