
from unittest import TestCase, skip 
from flask_restx import Resource, Api

import API.endpoints as ep


class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
       
        self.assertTrue(True) 
