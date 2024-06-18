# app.py
from flask import Flask
from config import Config
from extensions import db, migrate, jwt
from model import error_handling
from route.auth_route import auth_bp
from route.default_route import default_bp
from route.user_route import user_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialization extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Registration blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(default_bp)
    app.register_blueprint(error_handling.error_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
