#!/usr/bin/python3
"""Starts a Flask web application.
Routes:
    /hbnb: HBnB home page.
"""
from flask import Flask, render_template, Markup

from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State

app = Flask(__name__)
"""The Flask application instance."""


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """The hbnb page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """The Flask app/request context end event listener."""
    storage.close()


if __name__ == "__main__":
    '''to run the Flask development server.'''
    app.run(host="0.0.0.0", port=5000)
