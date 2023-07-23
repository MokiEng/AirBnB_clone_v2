#!/usr/bin/python3
"""a script that starts a Flask web application:
Routes:
    /hbnb_filters: HBnB HTML filters page.
"""
from flask import Flask, render_template

from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)
"""The Flask application instance."""


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """The hbnb_filters page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """The Flask app/request context end event listener."""
    storage.close()


if __name__ == "__main__":
    '''to run the Flask development server.'''
    app.run(host="0.0.0.0", port=5000)
