from app import app, auth
from model.user_model import user_model
from flask import request

obj = user_model()

# GETS
@app.route('/books/getall')
@auth.login_required
def books_getall_controller():
    return obj.books_getall_model()


# POSTS
@app.route('/books/add', methods=['POST'])
@auth.login_required
def books_add_controller():
    return obj.books_add_model(request.form)


# PUTS
@app.route('/books/update', methods=['PUT'])
@auth.login_required
def books_update_controller():
    return obj.books_update_model(request.form)


# DELETES
@app.route('/books/delete/<id>', methods=['DELETE'])
@auth.login_required
def books_delete_controller(id):
    return obj.books_delete_model(id)