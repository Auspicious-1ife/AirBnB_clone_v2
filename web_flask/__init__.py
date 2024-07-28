#!/usr/bin/python3
"""
A simple Flask web application that listens on 0.0.0.0, port 5000
and displays 'Hello HBNB!' on the root route.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that returns 'Hello HBNB!'
    """
    return "Hello HBNB!"
