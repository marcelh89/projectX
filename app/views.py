""" VIEWS """

from flask import render_template
from app import app


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/randomdates")
def random():
    return render_template('dates.html', id=1)
