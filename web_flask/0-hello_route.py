#!/usr/bin/python3
"""
A script to run the Flask web application.
"""

from web_flask import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
