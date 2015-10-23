import os.path
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
