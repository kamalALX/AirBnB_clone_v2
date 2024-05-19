#!/usr/bin/python3
""" flask storage docs """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """Displays a HTML page"""
    states = storage.all(State).values()
    ok = 2
    return render_template("9-states.html", states=states, ok=ok)


@app.route("/states/<id>", strict_slashes=False)
def states_list_id(id):
    """Displays a HTML page"""
    states = storage.all(State).values()
    ok = 0
    idied_state = None
    for state in states:
        if state.id == id:
            idied_state = state
            ok = 1
    return render_template("9-states.html", states=idied_state, ok=ok)


@app.teardown_appcontext
def teardown(exception):
    """close connection"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
