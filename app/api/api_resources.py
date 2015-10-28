__author__ = 'marcman'

import arrow
import json
from flask import Flask, request
from flask_restful import Resource
from database.shortitem import Shortitem

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class api_randomdates(Resource):
    def get(self):
        data = {}

        dates_list = []
        for x in range(5):
            now = str(arrow.utcnow().format('YYYY-MM-DD HH:mm:ss'))
            dicEvent = {}
            dicEvent['date'] = now
            dates_list.append(dicEvent)
        data['dates'] = dates_list
        return json.dumps(data)  # from flask import jsonify geht nicht, subevents werden nicht angezeigt


class api_randomevents(Resource):
    def get(self):
        data = {}

        dates_list = []
        for x in range(5):
            now = str(arrow.utcnow().format('YYYY-MM-DD HH:mm:ss'))
            dicEvent = {}
            dicEvent['date'] = now
            dicEvent['name'] = 'eventFromApi' + str(x)
            dates_list.append(dicEvent)
        data['dates'] = dates_list
        return json.dumps(data)  # from flask import jsonify geht nicht, subevents werden nicht angezeigt

class api_shortitems(Resource):
    def get(self):

        items = []
        for shortitem in Shortitem.objects():
            item = {}
            item['message'] = shortitem.message
            item['created'] = str(shortitem.created)
            items.append(item)
        return json.dumps(items)

    def post(self):
        val = request.form['val']
        shortItem = Shortitem(message=val).save()
        return ""
