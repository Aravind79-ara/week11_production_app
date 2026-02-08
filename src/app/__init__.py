from flask import Flask
from .extensions import db
from .routes import api
import os

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///fallback.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev")

    db.init_app(app)
    app.register_blueprint(api)

    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    return app