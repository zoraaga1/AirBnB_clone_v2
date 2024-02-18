#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route that displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Route that displays 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Route that displays 'C ' followed by the value of the text variable."""
    return 'C ' + (text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
