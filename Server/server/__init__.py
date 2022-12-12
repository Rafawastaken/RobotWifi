from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import json


app = Flask(__name__)

with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db" 

    db = SQLAlchemy(app)

    # API Blueprints
    from .api import api_bp
    api = Api(api_bp)
    app.register_blueprint(api_bp)

    # Api endpoints
    from .api import ComunicarRobot
    api.add_resource(ComunicarRobot, '/robot-com')
