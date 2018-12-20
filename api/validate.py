from flask import Flask, jsonify, request, Response
import datetime

import re

from api.models import user_list, incident_inventory


class Validation:
    def validate_user_not_found(self, UserId):
        users = []
        for user in users:
            if user["UserId"] == UserId:
                users.append({
                    "message": "user exists"
                }), 200
            else:
                if user["UserId"] != UserId:
                    users.append({"message": "User not found"}), 204
        return users

    def validate_add_red_flag(self, **args): 

        id = len(user_list)+1,
        createdOn = args.get('createdOn'),
        createdBy = args.get('createdBy'),
        # incident_type = args.get('incident_type'),
        location = args.get('location'),
        status = args.get('draft'),
        Images = args.get('Images'),
        Videos = args.get(' Videos'),
        comment = args.get('comment')

        if createdOn:
            datetime = "%Y-%m-%d"
            return jsonify({"message": datetime}), 200
        elif not createdOn:
            return jsonify({"message": "enter date"}), 400

        if not createdBy or createdBy is " ":
            return jsonify({
                "message": "oops field cannot be empty"
            }), 400
        elif createdBy != int:
            return jsonify({"message": "createdBy should be integers"}), 400
        elif not location or location is " ":
            return jsonify({
                "message": "oops lastname required and cannot be empty"
            }), 400
        elif not comment or comment is " ":
            return jsonify({
                "message": "oops othernames required and cannot be empty"
            }), 400

        if not id or len(id) == 0:
            return jsonify({
                "message": "oops  id required"
            }), 400
        elif id is not int:
            return jsonify({
                "message": "oops  id has to be a set of integers"
            }), 400

        if not Images or Images is " ":
            return jsonify({"message": "Email field can not be empty"}), 400
        elif not Videos or Videos is "":
            return jsonify({"message": "Enter a valid email address"}), 400

        if not status or status is " ":
            return jsonify({"message": "Status field can not be empty"}), 400
        elif status == int:
           return jsonify({
                "message": "oops status should be a list of characters"
            }), 400

        else:
            return jsonify({"message":"some fields are missing"})

    def validate_add_user(self, **args):
        users = []

        # data = request.get_json()
        # UserId =  len(users)+1,

        firstname = args.get("firstname"),
        lastname = args.get("lastname"),
        othernames = args.get("othernames"),
        email = args.get("email"),
        phoneNumber = args.get("phoneNumber"),
        username = args.get("username"),

        # registered = kwargs["registered"],
        # isAdmin = kwargs["isAdmin"]

        if not firstname or firstname is " ":
            users.append({
                "message": "oops firstname required and cannot be empty"
            }), 400
        elif not lastname or lastname is " ":
            users.append({
                "message": "oops lastname required and cannot be empty"
            }), 400
        elif not othernames or othernames is " ":
            users.append({
                "message": "oops othernames required and cannot be empty"
            }), 400

        if not phoneNumber or len(phoneNumber) == 0:
            users.append({
                "message": "oops  phoneNumber required"
            }), 400
        elif phoneNumber is not int:
            users.append({
                "message": "oops  phoneNumber has to be a set of integers"
            }), 400

        if not email or email is " ":
            users.append({'message': 'Email field can not be empty.'}), 400
        elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            users.append({'message': 'Enter a valid email address.'}), 400

        if not username or username is " ":
            users.append({'message': 'Username field can not be empty.'}), 400
        elif type(username) == int:
            users.append({
                "message": "oops username should be a list of characters"
            }), 400

        return users

    def validate_userId(self, userId, user):
        userId = []
        if type(userId) != int:
            userId.append({
                "message": "oops userId should be an integer "
            }), 400

        if not user or len(user_list) == 0:
            userId.append({
                "message": "oops user_list empty"
            }), 400
        return userId

    @staticmethod
    def validate_red_flag(self, red_flag):
        validations = []

        if not red_flag['id']:
            validations.append({'message': 'id is required'})
        else:
            if not isinstance(red_flag['id'], int):
                validations.append({'message': 'Enter a valid id'})

        if not red_flag['createdBy'] or red_flag['createdBy'].isspace():
            validations.append({'message': ' User is required'})

        return validations

    def validate_id(self, id):
        id = []
        if not id or id < 1:
            id.append({
                "message": "oops id required and canot be less than one"
            }), 400
        return id
