from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # with app.app_context():
    #     # Include our Routes
    #     from . import routes

    #     # Register Blueprints
    #     app.register_blueprint(auth.auth_bp)
    #     app.register_blueprint(admin.admin_bp)
    return app