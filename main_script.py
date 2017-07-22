'__author__' == 'cyril'


from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello from the other side"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST site"
    else:
        return "GET Site"


@app.route('/hello')
def hello(name=None):
    name = "Cyril"
    return render_template('hello.html', name=name)
