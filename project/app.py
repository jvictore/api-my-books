from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask import make_response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/myBooks'
auth = HTTPBasicAuth()

db = SQLAlchemy(app)

@auth.verify_password
def authenticate (username, password):
    if username and password:
        if username == 'user' and password == '1234':
            return True
    return False

from controller import *

@app.route('/')
@auth.login_required
def welcome():
    return make_response({
  "Possible routes": [
    "/books/getall",
    "/books/getone/<id>",
    "/books/gettotalpages",
    "/books/add",
    "/books/update",
    "/books/delete/<id>"
  ]
}, 200)