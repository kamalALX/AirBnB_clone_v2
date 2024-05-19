#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def route_states():
        pep_fix = models.dummy_classes["State"]
        data = models.storage.all(cls=pep_fix)
        states = data.values()
        return render_template('7-states_list.html', states_list=states)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
