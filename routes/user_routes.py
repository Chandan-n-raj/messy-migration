# routes/user_routes.py
from flask import Blueprint, request, jsonify
from services import user_service

bp = Blueprint("users", __name__)

@bp.route("/", methods=["GET"])
def health():
    return {"status": "ok"}

@bp.route("/users", methods=["GET"])
def list_users():
    return jsonify(user_service.get_all_users())

@bp.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify(user_service.get_user_by_id(user_id))

@bp.route("/users", methods=["POST"])
def create():
    data = request.get_json()
    return jsonify(user_service.create_user(data.get("name"), data.get("email"), data.get("password"))), 201

@bp.route("/user/<int:user_id>", methods=["PUT"])
def update(user_id):
    data = request.get_json()
    return jsonify(user_service.update_user(user_id, data.get("name"), data.get("email")))

@bp.route("/user/<int:user_id>", methods=["DELETE"])
def delete(user_id):
    return jsonify(user_service.delete_user(user_id))

@bp.route("/search", methods=["GET"])
def search():
    name = request.args.get("name", "")
    return jsonify(user_service.search_users(name))

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return jsonify(user_service.login(data.get("email"), data.get("password")))
