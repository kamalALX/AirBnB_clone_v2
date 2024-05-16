#!/usr/bin/python3
""" A minimal flask application """
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


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pypy(text):
    """ Display a message starting with 'python' followed
        by the provided text.
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run()
