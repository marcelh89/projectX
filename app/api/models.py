__author__ = 'marcman'

import arrow
from flask import jsonify
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class api_randomevents(Resource):
    def get(self):
        data = {}

        dates_list = []
        for x in range(5):
            now = str(arrow.utcnow().format('YYYY-MM-DD HH:mm:ss'))
            dicEvent = {}
            dicEvent['date'] = now
            dates_list.append(dicEvent)
        data['dates'] = dates_list
        return jsonify(data)
