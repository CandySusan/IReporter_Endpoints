from flask import jsonify, request
from api.models import incident_inventory,Record
from api.validate import Validation

validate=Validation()

red_flags = []
class Controller:

    def add_red_flag_record(self):
        """this function adds a red-flag to the incident_inventory"""

        request_data = request.get_json()

        id = len(red_flags)+1,
        createdBy = request_data.get('createdBy')
        incident_type = request_data.get('incident_type')
        location = request_data.get('location')
        images = request_data.get('images')
        videos = request_data.get('videos')
        comment = request_data.get('comment')
         
        args_strings = [createdBy,incident_type,location,images,videos,comment]

        # if args_strings:
        #     return jsonify({"error":"fields missing"}),400
        # return jsonify({"message":"fields satisfied"}),200

        red_flag_record = Record(createdBy=createdBy,incident_type=incident_type,
        location=location,images=images,videos=videos,comment=comment)
        incident_inventory.append(red_flag_record.red_flag_dict())
        return jsonify({"status":201,"data":[{"data":red_flag_record.red_flag_dict(),
        "message":"Red flag record created successfully"}]}),201
        
