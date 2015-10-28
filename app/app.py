""" APP """

from flask import Flask, jsonify
from flask_restful import Resource, Api
from api import api
from flask.ext.mongoengine import MongoEngine
import os


app = Flask(__name__)
app.config.from_object('config')
app.config['MONGODB_SETTINGS'] = {
    'db': 'projectx',
    'host': os.environ['HOSTNAMEMONGO'],
    'port': 27017
}
db = MongoEngine(app)

""" API """
api = api.setup_api(app)
