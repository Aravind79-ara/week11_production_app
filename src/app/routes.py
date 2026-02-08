from flask import Blueprint

api = Blueprint("api", __name__)

@api.route("/api/ping")
def ping():
    return {"message": "Production_app"}