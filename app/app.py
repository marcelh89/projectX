""" APP """

from flask import Flask, jsonify
from flask_restful import Resource, Api
from api import api

app = Flask(__name__)
app.config.from_object('config')

""" API """
api = api.setup_api(app)
