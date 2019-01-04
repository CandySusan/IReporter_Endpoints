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
        return jsonify({
                "status":201,
                "data":[{
                    "red_flag_id":red_flag_id,
                     "message":"Red flag record created successfully"
                    }]
                }),201
  
    def get_all_red_flags(self):
        """this function returns incident_inventory"""
        if len(incident_inventory) == 0:
           return jsonify({
            "status": 400,
            "error": "Red_flag record not found"
            }), 400
        return jsonify({
        "status": 200,
        "data": [redflag for redflag in incident_inventory],
         }), 200

    def get_specific_red_flag_record(self,red_flag_id):
        """this function returns a specific red_flag record"""
        if len(incident_inventory) == 0:
            return jsonify({
                "status": 400,
                "message": "Red_Flag record not found!"
                }), 400
        for red_flag in incident_inventory:
            if red_flag[0]['red_flag_id'] == red_flag_id:  
               return jsonify({
                   "status": 200,
                   "data": red_flag
                   }), 200
            return jsonify({
                    "error": "Record doesnot exist!!",
                    "status":404
                    }),404        

    def delete_specific_red_flag_record(self,red_flag_id):
        """This method removes the red-flag record from a list using the id"""
        if len(incident_inventory) == 0:
            return jsonify({
                    "status": 400,
                    "message": "Red_Flag record not found!"
                    }), 400 
        for red_flag  in incident_inventory:
            if red_flag[0]['red_flag_id'] == red_flag_id:
                    incident_inventory.remove(red_flag)
                    return jsonify({
                        "status": 200, 
                        "data": [{"red_flag_id": red_flag_id, 
                        "message": "red-flag record has been deleted"
                        }]}), 200
            return jsonify({
                    "error": "Record doesnot exist!!",
                    "status":404
                    }),404

    def edit_location_of_specific_red_flag_record(self):
        data = json.loads(request.data)
        location = data.get('location')
        red_flag_id = data.get('red_flag_id')
        red_flag_id = int(red_flag_id)
        for redflag in incident_inventory:
            if int(redflag['red_flag_id']) == red_flag_id:
                if redflag['status'] != 'draft':
                    return jsonify({
                    'status': 400,
                    'message': 'Only draft status can be updated!'}), 400
            redflag['location'] = location
            return jsonify({
                'status': 200, 
                'data':[{
                    "red_flag_id":red_flag_id,
                    "message": "Updated red-flag record’s location"
                        }]
                }), 200
        return jsonify({"status": 404,
                    "error": "Record doesnot exist!!"
                    }), 404




    
   
            
    