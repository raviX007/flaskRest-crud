from flask import Flask
from models import mongo
from views import user

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = "mongodb://db:27017/Users"
    mongo.init_app(app)

    app.register_blueprint(user, url_prefix='/api')

    return app
