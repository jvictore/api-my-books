from flask import make_response
import mysql.connector
import json

class user_model():
    def __init__(self):
        # Connections
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="maracuja123", database="api-my-books")
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print("Connection Successful")

        except:
            print("Some error.")

    def books_getall_model(self):
        # Query execution code
        self.cur.execute("SELECT * FROM books;")
        result = self.cur.fetchall()
        if len(result) > 0:
            return  make_response({"result": result}, 200)
            # return json.dumps(result)
        else:
            return make_response({"message": "No data found"}, 204)

    def books_add_model(self, data):
        self.cur.execute(f"INSERT INTO books(name, author, language, genre, publisher, publication_date, pages) VALUES ('{data['name']}', '{data['author']}', '{data['language']}', '{data['genre']}', '{data['publisher']}', '{data['publication_date']}', '{data['pages']}')")
        return make_response({"message": "Book added successfully."}, 201)

    def books_update_model(self, data):
        self.cur.execute(f"UPDATE books SET name='{data['name']}', author='{data['author']}', language='{data['language']}', genre='{data['genre']}', publisher='{data['publisher']}', publication_date='{data['publication_date']}', pages='{data['pages']}' WHERE id='{data['id']}'")
        if self.cur.rowcount > 0:
            return make_response({"message": "Book updated successfully."}, 201)
        else:
            return make_response({"message": "Nothing to update."}, 202)

    def books_delete_model(self, id):
        self.cur.execute(f"DELETE FROM books WHERE id={id}")
        if self.cur.rowcount > 0:
            return make_response({"message": "Book deleted successfully."}, 200)
        else:
            return make_response({"message": "Nothing to delete."}, 202)