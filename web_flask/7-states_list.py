#!/usr/bin/python3
""" a script that starts a Flask web application:
Routes:
    /states_list: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage sorted
        by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)
'''The Flask application instance.'''


@app.route("/states_list", strict_slashes=False)
def states_list():
    """The states_list page."""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """The Flask app/request context end event listener."""
    storage.close()


if __name__ == "__main__":
    '''to run the Flask development server.'''
    app.run(host="0.0.0.0", port=5000)
