from flask import jsonify, request,Response
from api.models import incident_inventory,Record
from api.validate import Validation
import json

validate=Validation()
incident_inventory=[]
red_flags = []  
class Controller:

    def add_red_flag_record(self):
        """this function adds a red-flag to the incident_inventory"""
       

        request_data = request.get_json()
        red_flag_id = len(red_flags)+1,
        createdBy = request_data.get('createdBy')
        incident_type = request_data.get('incident_type')
        location = request_data.get('location')
        images = request_data.get('images')
        videos = request_data.get('videos')
        comment = request_data.get('comment')
         
        # args_strings = [createdBy,incident_type,location,images,videos,comment]
        # if not args_strings:
        #     return jsonify({"error":"fields missing"}),400
        # return jsonify({"message":"fields satisfied"}),200

        red_flag_record = Record(createdBy=createdBy,incident_type=incident_type,
        location=location,images=images,videos=videos,comment=comment)
        incident_inventory.append(red_flag_record.red_flag_dict())
        return incident_inventory


    def get_all_red_flags(self):
        """this function returns incident_inventory"""
        controller=Controller()
        get_all_red_flags =controller.add_red_flag_record()
        return get_all_red_flags

    def get_specific_red_flag_record(self,red_flag_id):
        """this function returns a specific red_flag record"""

        controller=Controller()
        for red_flag in incident_inventory:
            if red_flag['red_flag_id'] == red_flag_id:
                    if red_flag is None:
                        return controller.response_unaccepted("none")
            return red_flag
                

    def delete_specific_red_flag_record(self,red_flag_id):
        """This method removes the red-flag record from a list using the id"""
        
        for red_flag  in incident_inventory:
            if red_flag['red_flag_id'] == red_flag_id:
                if red_flag is None:
                    incident_inventory.remove(red_flag)
                return "red-flag record has been deleted"
            return red_flag


    def response_emptystring(self):
        return Response(json.dumps({
            "status": 400,
            "message": "No empty fields are allowed"
        }), content_type="application/json", status=400)

    def response_unaccepted(self, word):
        if word == "none":
            status_code = 404
            message = "no red-flag with such an id"
        elif word == "status":
            status_code = 404
            message = "Wrong Status given"
        elif word == "empty":
            status_code = 400
            message = "No empty fields are allowed"
        else:
            status_code = 400
            message = "Unaccepted datatype or Inavlid Redflag"
        return Response(json.dumps({
            "status": status_code,
            "message": message
        }), content_type="application/json", status=status_code)

    def response_sumission_success(self, return_data, keyword):
        if keyword == "delete":
            message = "red-flag record has been deleted"
        else:
            message = "Updated red-flag record’s location"
        return Response(json.dumps({
            "status": 200,
            "data": [return_data],
            "message": message
        }), content_type="application/json", status=200)

    def create_id(self, get_redflags_id):
        if not get_redflags_id:
            return 1
        else:
            return 1 + get_redflags_id[-1].get("red_flag_id")
            
