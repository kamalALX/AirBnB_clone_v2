#!/usr/bin/python3
""" minimal flask application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ this methode displays a string in the route / """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ this methode displays a string in the route /hbnb """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """ this methode displays a string in the route /c/<text> """
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run()
