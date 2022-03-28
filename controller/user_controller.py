from app import app
from model.user_model import user_model
from flask import request

obj = user_model()

@app.route('/books/getall')
def books_getall_controller():
    return obj.books_getall_model()

@app.route('/books/add', methods=['POST'])
def books_add_controller():
    return obj.books_add_model(request.form)

@app.route('/books/update', methods=['PUT'])
def books_update_controller():
    return obj.books_update_model(request.form)

@app.route('/books/delete/<id>', methods=['DELETE'])
def books_delete_controller(id):
    return obj.books_delete_model(id)