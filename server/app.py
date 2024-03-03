# app.py

import datetime
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from main import main_bp
from auth import jwt, bcrypt, auth_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
    app.config['SECRET_KEY'] = 'edwevfsvfgvdc3'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    migrate = Migrate(app, db)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    CORS(app, resources={r"*": {"origins": "*"}})

    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=5555, debug=True)
