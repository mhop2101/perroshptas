from flask import Flask, render_template
from script import get_available_room
import json
app = Flask(__name__)


@app.route('/')
def hello_world():

    with open('info.json', 'r') as content:
        info = json.load(content)

    ml = get_available_room('.ML', info)
    ll = get_available_room('.LL', info)
    c = get_available_room('.C_', info)
    sd = get_available_room('.SD', info)

    return render_template('index.html',
                           ml=ml,
                           ll=ll,
                           c=c,
                           sd=sd)


if __name__ == '__main__':
    app.run(debug=True)
