from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash
from bson.objectid import ObjectId

mongo = PyMongo()

class UserModel:
    @staticmethod
    def create_user(name, email, password):
        hashed_password = generate_password_hash(password)
        user_data = {
            'name': name,
            'email': email,
            'password': hashed_password
        }
        return mongo.db.user.insert_one(user_data)

    @staticmethod
    def get_user_by_id(user_id):
        return mongo.db.user.find_one({'_id': ObjectId(user_id)})

    @staticmethod
    def get_all_users():
        return list(mongo.db.user.find())

    @staticmethod
    def update_user(user_id, name, email, password):
        hashed_password = generate_password_hash(password)
        return mongo.db.user.update_one(
            {'_id': ObjectId(user_id)},
            {'$set': {'name': name, 'email': email, 'password': hashed_password}}
        )

    @staticmethod
    def delete_user(user_id):
        return mongo.db.user.delete_one({'_id': ObjectId(user_id)})
