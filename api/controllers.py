from flask import jsonify, request
from api.models import incident_inventory,Record
from api.validate import Validation

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
       
        

        for red_flag in incident_inventory:
            if red_flag['red_flag_id'] == red_flag_id:
                return incident_inventory