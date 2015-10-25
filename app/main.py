"""
hauptanwendung, zieht sich alle abhaengigkeiten

datenbankvorbereitung, ausfuehren mit `python app.py`

"""
from app import app  # , db

# from app.models import *
from views import *

'''admin.setup()
api.setup()


def create_tables():
    # Create table for each model if it does not exist.
    # Use the underlying peewee database object instead of the
    # flask-peewee database wrapper:
    db.database.create_tables([Event], safe=True)'''

if __name__ == '__main__':
    # create_tables()
    app.run(host='0.0.0.0', port=5000, debug=True)
