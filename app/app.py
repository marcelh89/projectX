import os.path
import arrow
import json
from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


""" VIEWS """
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/randomdates")
def random():
    return render_template('dates.html', id=1)

""" API """
@app.route('/api/randomevents', methods=['GET'])
def api_randomevents():
    data = {}
    dates_list = []
    for x in range(5):
        now = str(arrow.utcnow().format('YYYY-MM-DD HH:mm:ss'))
        dicEvent = {}
        dicEvent['date'] = now
        dates_list.append(dicEvent)
    data['dates'] = dates_list
    return json.dumps(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
