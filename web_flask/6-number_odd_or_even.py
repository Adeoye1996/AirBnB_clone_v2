#!/usr/bin/python3
"""
Start Flask application.

This script initializes a Flask application and defines multiple routes:
- '/' returns 'Hello HBNB!'
- '/hbnb' returns 'HBNB'
- '/c/<text>' returns 'C ' followed by the value of the text variable
- with underscores replaced by spaces
- '/python' or '/python/<text>' returns 'Python ' followed by the value
- of the text variable with underscores replaced by spaces (default is 'is cool')
- '/number/<int:n>' returns '<n> is a number' only if n is an integer
- '/number_template/<int:n>' displays an HTML page only if n is an integer
- '/number_odd_or_even/<int:n>' displays an HTML page only if n is an integer
- and indicates if n is odd or even
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Return 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Display 'C ' followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Display 'Python ' followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """Display '<n> is a number' only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display an HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display an HTML page only if n is an integer and indicate if n is odd or even"""
    evenness = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenness=evenness)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
