__author__ = 'marcman'


import os.path
import app
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_app_exists(self):
        app_exists = os.path.isfile('app/app.py')
        assert app_exists

if __name__ == '__main__':
    unittest.main()
