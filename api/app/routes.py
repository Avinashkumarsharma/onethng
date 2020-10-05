from flask import current_app as app
from flask import request
from app.models import User
from app import db
@app.route('/')
def home():
    return "Welcome Home"
@app.route('/v1')
def v1():
    return "Welcome Home v1"
@app.route('/test')
def dev():
    user = User()
    con = db.get_db()
    response = list(con.tables.all())
    return "Welcome Home dev" + user.showname() + " " + str(response)
@app.route('/v1/dev')
def dev2():
    userid = request.headers.get('user_id')
    return "Welcome Home v1 dev " + str(request.headers)

