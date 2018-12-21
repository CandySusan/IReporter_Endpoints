from flask import jsonify, request
from api.models import incident_inventory, user_list, Record

from api.validate import Validation

validate=Validation()


class Controller:

    def add_red_flag_record(self):
        """this function adds a red-flag to the incident_inventory"""

        red_flags = []

        request_data = request.get_json()
<<<<<<< HEAD
        print (request_data)
=======
        
        
>>>>>>> develop
        id = len(red_flags)+1,
        createdBy = request_data['createdBy'],
        incident_type = request_data['incident_type'],
        location = request_data['location'],
        images = request_data['images'],
        videos = request_data['videos'],
        comment = request_data['comment']
        red_flag_record = Record(id=id,createdBy=createdBy,incident_type=incident_type,location=location,images=images,videos=videos,comment=comment)
        validate = Validation.validate_add_red_flag(red_flag_record)
        if  validate == "validated":
                    #    return jsonify({"status":400,"message":"Some fields missing"}),400
            valid_red_flag = Record.red_flag_dict(self)
            incident_inventory.append(valid_red_flag)
            return jsonify({"status":201,"message":"Created successfully"}),201
        else:
            return validate

        # validateReedflag = RedflagClass.func(data);
        # if validateReedflag == "falg valid":
        #     passDataToModelsAndSave;
        #     return jsonify ({'message':'whaterver'}), 201
        # else:
        #     return validateReedflag
