__author__ = 'devnull'
from mongoengine import *
import datetime

class Shortitem(Document):
    created = DateTimeField(default=datetime.datetime.now)
    message = StringField()

    meta = {
        'indexes': [
            {'fields': ['created'], 'expireAfterSeconds': 5}
        ]
    }