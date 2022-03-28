from flask import make_response
import mysql.connector
import json

class user_model():
    def __init__(self):
        # Connections establishment code
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="maracuja123", database="flask_tutorial")
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print("Connection Successful")

        except:
            print("Some error.")

    def user_getall_model(self):
        # Query execution code
        self.cur.execute("SELECT * FROM users;")
        result = self.cur.fetchall()
        if len(result) > 0:
            return  make_response({"payload": result}, 200)
            # return json.dumps(result)
        else:
            return make_response({"message": "No data found"}, 204)

    def user_addone_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES ('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        return make_response({"message": "User created successfully."}, 201)

    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id='{data['id']}'")
        if self.cur.rowcount > 0:
            return make_response({"message": "User updated successfully."}, 201)
        else:
            return make_response({"message": "Nothing to update."}, 202)

    def user_delete_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount > 0:
            return make_response({"message": "User deleted successfully."}, 200)
        else:
            return make_response({"message": "Nothing to delete."}, 202)