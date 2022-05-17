from socket import socket
import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
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
    pages = db.Column(db.Integer)
    

    def to_json(self):
        return {"id": self.id,
                "author": self.author,
                "genre": self.genre,
                "language": self.language,
                "name": self.name,
                "publication_date": self.publication_date,
                "publisher": self.publisher,
                "pages": self.pages}

    def get_all(self):
        books_objeto = self.query.all()
        books_json = [book.to_json() for book in books_objeto]
        final_json = json.dumps(books_json)

        return Response(final_json)

    def get_all_author(self, data):
        author = data['author'].title().strip()
        books_objeto = self.query.filter_by(author=author)
        books_json = [book.to_json() for book in books_objeto]
        final_json = json.dumps(books_json)

        return Response(final_json)

    def get_all_publisher(self, data):
        publisher = data['publisher'].title().strip()
        books_objeto = self.query.filter_by(publisher=publisher)
        books_json = [book.to_json() for book in books_objeto]
        final_json = json.dumps(books_json)

        return Response(final_json)

    def get_one_id(self, id):
        books_objeto = self.query.filter_by(id=id).first()
        books_json = books_objeto.to_json()
        final_json = json.dumps(books_json)

        return Response(final_json)

    def get_one_name(self, data):
        name = data['name'].title().strip()
        books_objeto = self.query.filter_by(name=name).first()
        books_json = books_objeto.to_json()
        final_json = json.dumps(books_json)

        return Response(final_json)

    def get_total_pages(self):
        sum = db.session.query(db.func.sum(books.pages)).scalar()
        
        return Response({"total": sum })