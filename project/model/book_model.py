from socket import socket
import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask import make_response, Response
import json


db = SQLAlchemy()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
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


    # GETS
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
        pages = db.session.query(db.func.sum(Books.pages)).scalar()
        print(str(pages), file=sys.stderr)
        
        return make_response({"Total pages": pages }, 200)

    def get_total_reading_time(self, avg):
        pages = db.session.query(db.func.sum(Books.pages)).scalar()
        reading_time = int(pages) * int(avg)
        
        return make_response({"Reading time": reading_time }, 200)


    # POSTS
    def add(self, body):
        try:
            book = Books(author = body["author"],
                        genre = body["genre"],
                        language = body["language"],
                        name = body["name"],
                        publication_date = body["publication_date"],
                        publisher = body["publisher"],
                        pages = body["pages"]
                    )
            db.session.add(book)
            db.session.commit()
            return make_response({"message": "Book added successfully."}, 201)
        
        except Exception as e:
            print(str(e), file=sys.stderr)
            return make_response({"message": "Error adding the book."}, 400)

    # PUTS
    def update(self, body):
        book = Books.query.filter_by(id=body['id']).first()
        try:
            if ('author' in body):
                book.author = body['author']
            if ('genre' in body):
                book.genre = body['genre']
            if ('language' in body):
                book.language = body['language']
            if ('name' in body):
                book.name = body['name']
            if ('publication_date' in body):
                book.publication_date = body['publication_date']
            if ('publisher' in body):
                book.publisher = body['publisher']
            if ('pages' in body):
                book.pages = body['pages']
            db.session.add(book)
            db.session.commit()
            return make_response({"message": "Book updated successfully."}, 200)

        except Exception as e:
            print(str(e), file=sys.stderr)
            return make_response({'message': "Error updating the book."}, 400)

    # DELETE
    def remove_one_id(self, id):
        book = Books.query.filter_by(id=id).first()
        try:
            db.session.delete(book)
            db.session.commit()
            return make_response({"message": "Book deleted successfully."}, 200)
        except Exception as e:
            print(str(e), file=sys.stderr)
            return make_response({'message': "Error deleting the book."}, 400)