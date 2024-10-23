from flask import Blueprint, request, jsonify
from app.controllers import get_users, get_user, add_user, update_user, delete_user

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/users', methods=['GET'])
def fetch_users():
    users = get_users()
    return jsonify([{"id": user.user_id, "username": user.email} for user in users])

@api_blueprint.route('/users/<int:user_id>', methods=['GET'])
def fetch_user(user_id):
    user = get_user(user_id)
    if user:
        return jsonify({"user_id": user.user_id, "email": user.email})
    return jsonify({"error": "User not found"}), 404

@api_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = add_user(data['email'], data['password'])
    return jsonify({"id": user.user_id, "email": user.email}), 201

@api_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    data = request.json
    user = update_user(user_id, data.get('username'), data.get('password'))
    if user:
        return jsonify({"id": user.id, "username": user.username})
    return jsonify({"error": "User not found"}), 404

@api_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    user = delete_user(user_id)
    if user:
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404
