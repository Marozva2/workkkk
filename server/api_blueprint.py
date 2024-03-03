# api_blueprint.py

from flask import Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)
jwt = JWTManager()

