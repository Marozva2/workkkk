# main.py

from flask import Blueprint, jsonify
from flask_restful import Resource, Api
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from flask_jwt_extended import jwt_required

from models import User

main_bp = Blueprint('main', __name__)

api = Api(main_bp)


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User

    id = auto_field()
    firstname = auto_field()
    lastname = auto_field()
    email = auto_field()


user_schema = UserSchema()


class Example(Resource):

    @jwt_required()
    def get(self):
        # Example endpoint for user serialization
        users = User.query.all()
        serialized_users = [user_schema.dump(user) for user in users]
        return jsonify(serialized_users)


api.add_resource(Example, '/example')
