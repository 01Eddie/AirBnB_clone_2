#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)



@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """ Routes:
/hbnb_filters: display a HTML page like 6-index.html, which was done during the project 0x01. AirBnB clone - Web static
Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css from web_static/styles/ to the folder web_flask/static/styles
Copy files icon.png and logo.png from web_static/images/ to the folder web_flask/static/images
Update .popover class in 6-filters.css to allow scrolling in the popover and a max height of 300 pixels.
Use 6-index.html content as source code for the template 10-hbnb_filters.html:
Replace the content of the H4 tag under each filter title (H3 States and H3 Amenities) by &nbsp;
State, City and Amenity objects must be loaded from DBStorage and sorted by name (A->Z) """
    stateAll = storage.all("State").values()
    amenityAll = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html", stateAll=stateAll,amenityAll=amenityAll)