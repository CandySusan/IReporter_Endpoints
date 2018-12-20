from flask import Flask, jsonify, request, Response

# import re

from api.models import Record,  incident_inventory, User, user_list
from api.controllers import Controller
from api.validate import Validation

app = Flask(__name__)

controller = Controller()
# user_controller = User_controller()
validation = Validation()


@app.route('/')
def home_page():
    return "welcome to IReporter"


@app.route('/api/v1/redflags', methods=["POST"])
def create_red_flag_record():
    """this method creates the red_flags record"""
    redFlag = controller.add_red_flag_record(Record)
    return redFlag


# @app.route('/api/v1/redflags', methods=['GET'])
# def get_all_flag():
#     return jsonify({'message': "testing"})
