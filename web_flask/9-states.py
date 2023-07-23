#!/usr/bin/python3
"""a script that starts a Flask web application."""
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)
"""The Flask application instance."""


@app.route("/states", strict_slashes=False)
def states():
    """The states page.States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """display a HTML page: (inside the tag BODY)."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """The Flask app/request context end event listener."""
    storage.close()


if __name__ == "__main__":
    '''to run the Flask development server.'''
    app.run(host="0.0.0.0", port=5000)
