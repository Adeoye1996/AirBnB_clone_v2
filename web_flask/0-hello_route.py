#!/usr/bin/env python3
"""
Start a Flask application that returns 'Hello HBNB!' at the root URL.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns a greeting message."""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
