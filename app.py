from flask import Flask

app = Flask(__name__)

from controller import *

@app.route('/')
def welcome():
    return "My book API"