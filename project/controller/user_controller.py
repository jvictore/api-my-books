from app import app, auth
from app import app
from model.user_model import user_model
from model.book_model import Books

from flask import request, Response
import json
import sys
from flask_sqlalchemy import SQLAlchemy

obj = user_model()
obj2 = Books()

if __name__ == "__main__":
    app.run(host="0.0.0.0")

# GETS
@app.route('/books/getall')
@auth.login_required
def books_get_all_controller():
    return obj2.get_all()

@app.route('/books/getall/author')
@auth.login_required
def books_get_all_author_controller():
    return obj2.get_all_author(request.form)

@app.route('/books/getall/publisher')
@auth.login_required
def books_get_all_publisher_controller():
    return obj2.get_all_publisher(request.form)

@app.route('/books/getone/<id>')
@auth.login_required
def books_get_one_controller(id):
    return obj2.get_one_id(id)

@app.route('/books/getone/name')
@auth.login_required
def books_get_one_name_controller():
    return obj2.get_one_name(request.form)

@app.route('/books/gettotalpages')
@auth.login_required
def books_get_total_pages_controller():
    return obj2.get_total_pages()

@app.route('/books/gethours/<avgPerPage>')
@auth.login_required
def books_get_hours_controller(avgPerPage):
    return obj2.get_total_reading_time(avgPerPage)

# POSTS
@app.route('/books/add', methods=['POST'])
@auth.login_required
def books_add_controller():
    return obj2.add(request.get_json())


# PUTS
@app.route('/books/update', methods=['PUT'])
@auth.login_required
def books_update_controller():
    return obj2.update(request.get_json())


# DELETES
@app.route('/books/remove/<id>', methods=['DELETE'])
@auth.login_required
def books_remove_controller(id):
    return obj2.remove_one_id(id)

@app.route('/books/removeall', methods=['DELETE'])
@auth.login_required
def books_remove_all_controller():
    return obj.books_remove_all_model()