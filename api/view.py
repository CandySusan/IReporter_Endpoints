from flask import Flask
from api.models import Record,  incident_inventory, user_list
from api.controllers import Controller
from api.validate import Validation

app = Flask(__name__)

controller = Controller()
validation = Validation()


@app.route('/')
def home_page():
    return "welcome to IReporter"


"""this method creates the red_flags record"""


@app.route('/api/v1/redflags', methods=["POST"])
def create_red_flag_record():
    redFlag = controller.add_red_flag_record(Record)
    return redFlag


# @app.route('/api/v1/redflags', methods=['GET'])
# def get_all_flag():
#     pass
