#!/usr/bin/python3
"""Program that starts a Flask web application

App listens on 0.0.0.0 and port 5000
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB' """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
