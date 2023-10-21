#!/usr/bin/python3
""" this script for Add third view func that redirects and has default val for variable """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ this method for Returns some text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ this method for Return other text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ for replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ for replace more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
