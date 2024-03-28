#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask, render_template

app = Flask(__name__)
'''Instance of the web application'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''Home Page'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''hbnb page'''
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''C page'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''pyhton page'''
    return 'Python {}'.format(text.replace('_', ' '))
    
@app.route('/number/<int:n>')
def number_page(n):
    '''Number page.'''
    return '{} is a number'.format(n)
    
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """HTML page only if n is an integer and states whether n is odd or even"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
    
