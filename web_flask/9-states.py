#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def closeStorage(self):
    """ After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close() """
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(stateId=None):
    """ Routes:
    /states/<id>: display a HTML page: (inside the tag BODY)
    If a State object is found with this id:
    H1 tag: “State: ”
    H3 tag: “Cities:”
    UL tag: with the list of City objects linked to the State sorted by name (A->Z)
    LI tag: description of one City: <city.id>: <B><city.name></B>
    Otherwise:
    H1 tag: "Not found!" """
    states = storage.all("State")
    state = stateId
    if state is not None:
        state = "State." + state
    else:
        return render_template('9-states.html', states=states, stateId=stateId)


@app.teardown_appcontext
def closeStorage(self):
    """ After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close() """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

