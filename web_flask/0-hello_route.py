#!/usr/bin/python3
""" this Script for start a Flask web application """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ this method for Return some text. """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
