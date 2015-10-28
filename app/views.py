""" VIEWS """

from flask import render_template
from app import app


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/timeline")
def timeline():
    return render_template('timeline.html')\

@app.route("/expire")
def expire():
    return render_template('expire.html')

@app.route("/randomdates")
def randomdates():
    return render_template('dates.html', id=1)
