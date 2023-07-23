#!/usr/bin/python3
"""
a script that starts a Flask web application:
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage
        LI tag: description of one State: <state.id>:
                <B><state.name></B> + UL tag:with the list of City objects
                linked to the State sorted by name (A->Z)
              LI tag: description of one City: <city.id>: <B><city.name></B>
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)
"""The Flask application instance."""


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """The Flask app/request context end event listener"""
    storage.close()


if __name__ == "__main__":
    '''to run the Flask development server.'''
    app.run(host="0.0.0.0", port=5000)
