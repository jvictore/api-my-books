from enum import auto
from urllib import response
from flask import Flask, Response
from flask_httpauth import HTTPBasicAuth
from flask import make_response
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db:3306/myBooks'
# auth = HTTPBasicAuth()

db = SQLAlchemy(app)

class books(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  author = db.Column(db.String(100))
  genre = db.Column(db.String(100))
  language = db.Column(db.String(100))
  name = db.Column(db.String(100))
  publication_date = db.Column(db.String(100))
  publisher = db.Column(db.String(100))

  def to_json(self):
    return {"id": self.id,
            "author": self.author,
            "genre": self.genre,
            "language": self.language,
            "name": self.name,
            "publication_date": self.publication_date,
            "publisher": self.publisher}


@app.route("/livros", methods=["GET"])
def seleciona_livros():
  books_objeto = books.query.all()
  books_json = [book.to_json() for book in books_objeto]
  print(books_json)

  return Response(json.dumps(books_json))
  

app.run()





# @auth.verify_password
# def authenticate (username, password):
#     if username and password:
#         if username == 'user' and password == '1234':
#             return True
#     return False

# from controller import *

# @app.route('/')
# @auth.login_required
# def welcome():
#     return make_response({
#   "Possible routes": [
#     "/books/getall",
#     "/books/getone/<id>",
#     "/books/gettotalpages",
#     "/books/add",
#     "/books/update",
#     "/books/delete/<id>"
#   ]
# }, 200)