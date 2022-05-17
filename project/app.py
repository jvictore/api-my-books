from enum import auto
from urllib import response
from flask import Flask, Response
from flask_httpauth import HTTPBasicAuth
from flask import make_response
import json
from model.book_model import db


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db:3306/myBooks'
auth = HTTPBasicAuth()

db.init_app(app)



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