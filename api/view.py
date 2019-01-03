from flask import Flask, jsonify, request, Response,render_template

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
    return render_template("home.html")
   
   
@app.route('/api/v1/redflags', methods=["POST"])
def create_red_flag_record():
    """this method creates the red_flags record"""
    redFlag = controller.add_red_flag_record()
    if redFlag:
        return jsonify({"status":201,"data":[redFlag,{
     "message":"Red flag record created successfully"}]}),201
  

@app.route('/api/v1/redflags', methods=['GET'])
def get_all_flag():
    """this method gets all the red_flags records """
    redFlags = controller.get_all_red_flags()
    return jsonify({"status":200},redFlags),200


@app.route('/api/v1/redflags/<int:red_flag_id>', methods=['GET'])
def get_specific_red_flag_record(red_flag_id):
    """this method gets specific red_flags record """
    redFlags = controller.get_specific_red_flag_record(red_flag_id)
    return jsonify({"status":200,"data": [redFlags]}),200

       
@app.route('/api/v1/redflags/<int:red_flag_id>', methods=['DELETE'])
def delete_specific_red_flag_record(red_flag_id):
    """this method deletes specific red_flags record """
    return jsonify({"status": 200, "data": [{"id": red_flag_id, 
        "message": "red-flag record has been deleted"}]}), 200
        
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "The URL entered does not exist!!","status":404}),404


