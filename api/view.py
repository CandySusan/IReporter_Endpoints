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
def home_page():
    return "welcome to IReporter"


@app.route('/api/v1/redflags', methods=["POST"])
def create_red_flag_record():
    """this method creates the red_flags record"""
    redFlag = controller.add_red_flag_record()
    return jsonify({"status":201,"data":[redFlag,{
     "message":"Red flag record created successfully"}]}),201

@app.route('/api/v1/redflags', methods=['GET'])
def get_all_flag():
    """this method gets all the red_flags records """
    redFlags = controller.get_all_red_flags()
    return jsonify({"status":200},redFlags),200


@app.route('/api/v1/redflags/<int:red_flag_id>', methods=['GET'])
def get_specific_red_flag_record(red_flag_id):
    redFlags = controller.get_specific_red_flag_record(id)
    if not redFlags:
        return jsonify({"status": 404,"error": "redflag not found"}), 404
    return jsonify({"status":200},redFlags),200