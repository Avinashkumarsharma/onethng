from flask import Flask
from config import Config
def create_app(configoverride={}):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config.get_config())

    with app.app_context():
        # Include our Routes
        from . import routes

        # Register Blueprints
        # app.register_blueprint(auth.auth_bp)
        # app.register_blueprint(admin.admin_bp)
    return app