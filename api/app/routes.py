from flask import current_app as app
from flask import request
from app.models.user import User
from app import db
@app.route('/')
def home():
    return "Welcome Home"
@app.route('/v1')
def v1():
    return "Welcome Home v1"
@app.route('/test')
def dev():
    return "Welcome Home dev"
@app.route('/v1/dev')
def dev2():
    return "Welcome Home v1 dev " + str(request.headers)
@app.route('/ping')
def ping():
    return 'pong'

