from flask import Flask, jsonify, request
from api.models import incident_inventory, user_list

from api.validate import Validation

validate=Validation()


class Controller:

    def add_red_flag_record(self, Record):
        """this function adds a red-flag to the incident_inventory"""

        red_flags = []

        request_data = request.get_json()
        
        print (request_data)
        id = len(red_flags)+1,
        # createdOn =  request_data['createdOn'],
        createdBy = request_data['createdBy'],
        _type = request_data['type'],
        location = request_data['location'],

        Images = request_data['Images'],
        Videos = request_data['Videos'],
        comment = request_data['comment']

        red_flag = dict(

            Id=id,

            # createdOn = createdOn,
            createdBy=createdBy,
            type=_type,
            location=location,

            Images=Images,
            Videos=Videos,
            comment=comment
        )

        validate = Validation.validate_add_red_flag(self)
        if validate:
            return jsonify({"mesage":"Some fields missing"})
       
        incident_inventory.append(red_flag)
        return jsonify({"status":201,"message":"Created successfully"}),201

        # validateReedflag = RedflagClass.func(data);
        # if validateReedflag == "falg valid":
        #     passDataToModelsAndSave;
        #     return jsonify ({'message':'whaterver'}), 201
        # else:
        #     return validateReedflag
