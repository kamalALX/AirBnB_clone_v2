#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
import models

app = Flask("__name__")


@app.teardown_appcontext
def refresh(exception):
        models.storage.close()


@app.route("/states", strict_slashes=False)
def route_states():
        pep_fix = models.dummy_classes["State"]
        data = models.storage.all(cls=pep_fix)
        states = data.values()
        return render_template('7-states_list.html', states_list=states)


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


if __name__ == "__main__":
        app.run()
