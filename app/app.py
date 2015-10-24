import os.path
import arrow
import json
from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/randomdates")
def random():

    dates_list = []
    for x in range(5):
        now = str(arrow.utcnow().format('YYYY-MM-DD HH:mm:ss'))
        dates_list.append(now)

    return render_template('dates.html', dates = dates_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
