from flask import Flask
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
# auth = HTTPBasicAuth()

# @auth.verify_password
# def authenticate (username, password):
#     if username and password:
#         if username == 'jv' and password == '123':
#             return True
#     return False

from controller import *

@app.route('/')
# @auth.login_required
def welcome():
    return "My book API"