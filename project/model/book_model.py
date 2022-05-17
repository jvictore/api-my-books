from socket import socket
from flask_sqlalchemy import SQLAlchemy
from flask import make_response, Response
import json


db = SQLAlchemy()

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

    def get_all(self):
        books_objeto = self.query.all()
        books_json = [book.to_json() for book in books_objeto]

        return Response(json.dumps(books_json))
