# gotta have some tests!

# tests/test_basic.py

import os
import unittest
import json
from app import app


class BasicTests(unittest.TestCase):
    # setup and teardown #

    # exectued prior to each test
    def setUp(self):
        app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        self.app = app.test_client()
        self.app.testing = True
        pass

    # executed after tests
    def tearDown(self):
        pass

## TESTS ##

    def test_main_route(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_lookup_route_abbrv_result(self):
        response = self.app.get("/lookup/Florida", follow_redirects=True)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['states'][0]['abbrv'], "FL")

    def test_lookup_route_name_result(self):
        response = self.app.get("/lookup/Florida", follow_redirects=True)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['states'][0]['name'], "Florida")

    def test_lookup_route_response_code(self):
        response = self.app.get("/lookup/Florida", follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
