import hashlib
import random

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(name):
    app = Flask(name)
    rand_int = str(random.randint(1, 1001))
    app.secret_key = hashlib.sha256(rand_int.encode()).hexdigest()

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///viper.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False

    return app


app = create_app(__name__)
# create a db
db: SQLAlchemy = SQLAlchemy(app)
