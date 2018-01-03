# just a super simple server to support state type ahead lookups
from flask import Flask, jsonify
import csv
app = Flask(__name__)


class stateClass:  # the state class
    abbrv = ""
    name = ""

    def __init__(self, var1, var2):
        self.name = var1
        self.abbrv = var2

    def serialize(self):
        return {
            'name': self.name,
            'abbrv': self.abbrv
        }


states_list = []  # this holds the list of states


def matchStateName(x, state):  # perform the match (case insensitive)
    return x.name.lower().startswith(state.lower())


# this is just because
@app.route("/")
def hello_world():
    return "Hello, World!"


# the lookup route
@app.route("/lookup/<state>")
def lookup_state(state):
    results = [x.serialize() for x in states_list if matchStateName(x, state)]
    return jsonify({'states': results})


# load the states
with open('states.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        states_list.append(stateClass(row[0], row[1]))

# fire it up
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
