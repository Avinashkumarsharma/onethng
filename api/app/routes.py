from flask import current_app as app

@app.route('/ping')
def home():
    return "pong"
