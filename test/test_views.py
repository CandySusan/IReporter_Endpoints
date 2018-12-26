import unittest
import json
import random

from api.models import Record, User

from api.view import app

class TestApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.hostname = "/api/v1/"
        self.redflags ={
            "createdBy":1,
            "incident_type":"red_flag",
            "location" : "121421563" ,
            "images" : "[image, image]" ,
            "videos": "[image, image]" ,
            "comment" : "it's a pity"
                    }


    def test_invalid_url(self):
        response = self.client.get(self.hostname)
        self.assertEqual(response.status_code, 404)

    def test_add_red_flag_record(self):
        response = self.client.post(
            self.hostname+'redflags',
            content_type='application/json',
            data=json.dumps(self.redflags)
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
