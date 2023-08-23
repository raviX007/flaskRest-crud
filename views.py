from flask import Blueprint, jsonify, request
from models import UserModel

user = Blueprint('user', __name__)

@user.route('/users', methods=['GET'])
def get_All():
    users = UserModel.get_all_users()
    
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users), 200

@user.route('/user/<string:id>', methods=['GET'])
def get_By_Id(id):
    user = UserModel.get_user_by_id(id)
    if user:
        user['_id'] = str(user['_id'])  
        return jsonify(user), 200
    return jsonify(message='User not found'), 404

@user.route('/user', methods=['POST'])
def create():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not (name and email and password):
        return jsonify(message='Name, email, and password are required'), 400

    result = UserModel.create_user(name, email, password)
    if result.inserted_id:
        return jsonify(message='User created successfully'), 201
    return jsonify(message='Failed to create user'), 500

@user.route('/user/<string:id>', methods=['PUT'])
def update(id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not (name and email and password):
        return jsonify(message='Name, email, and password are required'), 400

    result = UserModel.update_user(id, name, email, password)
    if result.matched_count > 0:
        return jsonify(message='User updated successfully'), 200
    return jsonify(message='User not found'), 404

@user.route('/user/<string:id>', methods=['DELETE'])
def delete_By_Id(id):
    result = UserModel.delete_user(id)
    if result.deleted_count > 0:
        return jsonify(message='User deleted successfully'), 200
    return jsonify(message='User not found'), 404
