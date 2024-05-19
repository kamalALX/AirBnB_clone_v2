#!/usr/bin/python3
""" Flask application to display states list """
from models import storage
from flask import Flask, render_template
from collections import OrderedDict

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """ Display a HTML page with the list of states """
    original_dict = storage.all("State")
    new_dict ={}

    for key, value in original_dict.items():
        if 'name' in value:
            new_dict[value.name] = value.id

    sorted_dict = OrderedDict(sorted(new_dict.items()))
    return render_template('7-states_list.html', states=sorted_dict)

@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == '__main__':
    app.run()
