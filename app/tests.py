__author__ = 'marcman'

import os.path
import unittest


class ProjectXTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_app_exists(self):
        app_exists = os.path.isfile('app/main.py')
        assert app_exists


if __name__ == '__main__':
    unittest.main()
