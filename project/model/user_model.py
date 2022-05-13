from socket import socket
from flask import make_response
import sys

import time
import mysql.connector

class user_model():
    def __init__(self):
        # Connections
        try:
            time.sleep(10)
            self.con = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="myBooks",
                port=3306
            )
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print("Connection Successful", file=sys.stderr)

        except Exception as e:
            print("Some error in database connection", file=sys.stderr)
            print (e, file=sys.stderr, end='\n\n')

    # GETS
    def books_get_all_model(self):
        self.cur.execute("SELECT * FROM books;")
        result = self.cur.fetchall()

        if len(result) > 0:
            return  make_response({"result": result}, 200)
        else:
            return make_response({"message": "No data found"}, 204)

    def books_get_all_author_model(self, data):
        author = data['author'].title().strip()
        self.cur.execute(f"SELECT * FROM books WHERE author='{author}';")
        result = self.cur.fetchall()

        if len(result) > 0:
            return  make_response({"result": result}, 200)
        else:
            return make_response({"message": "No data found"}, 204)

    def books_get_all_publisher_model(self, data):
        publisher = data['publisher'].title().strip()
        self.cur.execute(f"SELECT * FROM books WHERE publisher='{publisher}';")
        result = self.cur.fetchall()

        if len(result) > 0:
            return  make_response({"result": result}, 200)
        else:
            return make_response({"message": "No data found"}, 204)

    def books_get_one_model(self, id):
        self.cur.execute(f"SELECT * FROM books WHERE id = {id};")
        result = self.cur.fetchall()

        if len(result) > 0:
            return  make_response({"result": result}, 200)
        else:
            return make_response({"message": "No data found"}, 204)


    def books_get_total_pages_model(self):
        self.cur.execute("SELECT pages FROM books;")
        result = self.cur.fetchall()
        sum = 0

        for page in result:
            sum += page['pages']

        if len(result) > 0:
            return  make_response({"total": sum }, 200)
        else:
            return make_response({"message": "No data found"}, 204)


    # POSTS 
    def books_add_model(self, data):
        # Capitalize the first letter to better compare in other routes
        author = data[author].title().strip()
        self.cur.execute(f"INSERT INTO books(name, author, language, genre, publisher, publication_date, pages) VALUES ('{data['name']}', '{author}', '{data['language']}', '{data['genre']}', '{data['publisher']}', '{data['publication_date']}', '{data['pages']}')")
        return make_response({"message": "Book added successfully."}, 201)


    # PUTS
    def books_update_model(self, data):
        if data.get('id'):
            if data.get('name'):
                self.cur.execute(f"UPDATE books SET name='{data.get('name')}' WHERE id='{data.get('id')}'")

            if data.get('author'):
                self.cur.execute(f"UPDATE books SET author='{data.get('author')}' WHERE id='{data.get('id')}'")

            if data.get('language'):
                self.cur.execute(f"UPDATE books SET language='{data.get('language')}' WHERE id='{data.get('id')}'")

            if data.get('genre'):
                self.cur.execute(f"UPDATE books SET genre='{data.get('genre')}' WHERE id='{data.get('id')}'")

            if data.get('publisher'):
                self.cur.execute(f"UPDATE books SET publisher='{data.get('publisher')}' WHERE id='{data.get('id')}'")

            if data.get('publication_date'):
                self.cur.execute(f"UPDATE books SET publication_date='{data.get('publication_date')}' WHERE id='{data.get('id')}'")

            if data.get('pages'):
                self.cur.execute(f"UPDATE books SET pages='{data.get('pages')}' WHERE id='{data.get('id')}'")
        
        else:
            return make_response({"message": "Field ID is missing. Nothing to update."}, 202)

        if self.cur.rowcount > 0:
            return make_response({"message": "Book updated successfully."}, 201)
        else:
            return make_response({"message": "Nothing to update."}, 202)

    
    # DELETES
    def books_remove_model(self, id):
        self.cur.execute(f"DELETE FROM books WHERE id={id}")
        if self.cur.rowcount > 0:
            return make_response({"message": "Book removed successfully."}, 200)
        else:
            return make_response({"message": "Nothing to remove."}, 202)

    def books_remove_all_model(self):
        self.cur.execute(f"DELETE FROM books;")
        if self.cur.rowcount > 0:
            return make_response({"message": "Books removed successfully."}, 200)
        else:
            return make_response({"message": "Nothing to remove."}, 202)