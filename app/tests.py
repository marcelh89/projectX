__author__ = 'marcman'

import os.path
import unittest


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_app_exists(self):
        app_exists = os.path.isfile('app/static_typing.py')
        assert app_exists


if __name__ == '__main__':
    unittest.main()
