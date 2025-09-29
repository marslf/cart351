from flask import Flask

app = Flask(__name__) # a python key term (anything with framed with _x_)

def index():
    return '<h1> Hello CART 351!</h1>'

