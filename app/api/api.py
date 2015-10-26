__author__ = 'marcman'

from flask_restful import Api
from .api_resources import *


# resourcen definieren
def setup_api(app):
    api = Api(app)

    api.add_resource(HelloWorld, '/api/')
    api.add_resource(api_randomdates, '/api/randomdates/')
    api.add_resource(api_randomevents, '/api/randomevents/')

    return api
