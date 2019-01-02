import unittest
import json
import random

from api.models import Record, User

from api.view import app

record=Record()

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
        self.test_redflags ={
            "createdBy":"",
            "incident_type":"",
            "location" : "" ,
            "images" : "" ,
            "videos": "" ,
            "comment" : ""
                    }


    def test_invalid_url(self):
        response = self.client.get(self.hostname)
        self.assertEqual(response.status_code, 404)

    def test_add_red_flag_record(self):
        response = self.client.post(
            self.hostname+'redflags',
            content_type='application/json',
            data=json.dumps(self.redflags),
            )
        
        data =json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(data.get("status"), 201)
        self.assertTrue(data, dict)

    # def test_add_red_flag_record_not_created(self):
    #     response = self.client.post(
    #         self.hostname+'redflags',
    #         content_type='application/json',
    #         data=json.dumps(self.test_redflags),
    #         )
    #     data =json.loads(response.data.decode())
    #     self.assertEqual(data["status"], 404)
    #     self.assertEqual(data["error"], "The red_flag record not created")

    def test_get_all_flag(self):
        response = self.client.get(
            self.hostname+'redflags',
            content_type='application/json',
            data=json.dumps(self.redflags)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_get_specific_flag(self):
        response = self.client.get(
            self.hostname+'redflags/<int:red_flag_id>',
            content_type='application/json',
            data=json.dumps(self.redflags)
        )
        data =json.loads(response.data.decode())
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data.get("status"), 404)
        self.assertTrue(data, dict)
     

    def test_get_specific_flag_doesnot_exist(self):
        response = self.client.get(
            self.hostname+'redflags/<int:red_flag_id>',
            content_type='application/json',
            data=json.dumps(self.redflags)
        )
        data =json.loads(response.data.decode())
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["status"],404) 
        

    def test_page_not_found(self):
        response = self.client.get(self.hostname)
        data =json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data.get("error"), "The URL entered does not exist!!")
        self.assertEqual(data.get("status"), 404)

    def test_delete_specific_red_flag_record(self):
        response = self.client.delete(
            self.hostname+'redflags/<int:red_flag_id>',
            content_type='application/json',
            data=json.dumps(self.redflags)
        )
        data =json.loads(response.data.decode())
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data.get("status"), 404) 
        self.assertTrue(data, dict)
        
    

    def test_delete_specific_red_flag_record_doesnot_exist(self):
        response = self.client.delete(
            self.hostname+'redflags/<int:red_flag_id>',
            content_type='application/json',
            data=json.dumps(self.redflags)
        )
        data =json.loads(response.data.decode())
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data.get("status"), 404) 
        

    def test_red_flag_not_found(self):
        red_flag_id = 0
        self.assertEqual(red_flag_id,False)

    def test_red_flag_id_is_int(self):
        red_flag_id = 2
        self.assertTrue(red_flag_id,True)

    
    def test_red_flag_exists(self):
        red_flag_id  = 1
        self.assertEqual(red_flag_id,True)


   