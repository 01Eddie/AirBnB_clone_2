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


@app.route("/cities_by_states", strict_slashes=False)
def citiesbystates(request):
    """ Routes:
/cities_by_states: display a HTML page: (inside the tag BODY)
H1 tag: “States”
UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
LI tag: description of one City: <city.id>: <B><city.name></B> """
    citystate = storage.all("State").values()
    return render_template('8-cities_by_states.html', citystate=citystate)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

