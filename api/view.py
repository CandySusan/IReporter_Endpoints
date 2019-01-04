from flask import Flask, jsonify, request, Response

# import re

from api.models import Record,  incident_inventory, User, user_list
from api.controllers import Controller
from api.validate import Validation
from api.models import Record

app = Flask(__name__)

controller = Controller()
validation = Validation()
record = Record


@app.route('/')
def Welcome():
    return jsonify({
        "message": "Welcome to Candy_IReporter",
        "status": 200
    }), 200


@app.route('/api/v1/redflags', methods=["POST"])
def create_red_flag_record():
    """this method creates the red_flags record"""
    redFlag = controller.add_red_flag_record()
    return redFlag


@app.route('/api/v1/redflags', methods=['GET'])
def get_all_flag():
    """this method gets all the red_flags records """
    redFlags = controller.get_all_red_flags()
    return redFlags


@app.route('/api/v1/redflags/<int:red_flag_id>', methods=['GET'])
def get_specific_red_flag_record(red_flag_id):
    """this method gets specific red_flags record """
    redFlags = controller.get_specific_red_flag_record(red_flag_id)
    return redFlags


@app.route('/api/v1/redflags/<int:red_flag_id>', methods=['DELETE'])
def delete_specific_red_flag_record(red_flag_id):
    """this method deletes specific red_flags record """
    del_red_flag = controller.delete_specific_red_flag_record(red_flag_id)
    return del_red_flag

@app.route('/api/v1/redflags/<int:red_flag_id>/location', methods=['PATCH'])
def edit_location_of_specific_red_flag_record(red_flag_id):
    edit_location = controller.edit_location_of_specific_red_flag_record()
    return edit_location

@app.route('/api/v1/redflags/<int:red_flag_id>/comment', methods=['PATCH'])
def edit_comment_of_specific_red_flag_record(red_flag_id):
    pass

@app.errorhandler(404)
def error_message(e):
    return jsonify({
        "error": "Record doesnot exist!!",
        "status": 404
    }), 404
