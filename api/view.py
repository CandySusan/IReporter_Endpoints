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
    return redFlag


# @app.route('/api/v1/redflags', methods=['GET'])
# def get_all_flag():
#     return jsonify({'message': "testing"})
