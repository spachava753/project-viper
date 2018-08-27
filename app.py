import hashlib
import random
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(name):
    flask_app = Flask(name)
    rand_int = str(random.randint(1, 1001))
    flask_app.secret_key = hashlib.sha256(rand_int.encode()).hexdigest()

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///viper.db'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_ECHO'] = False

    return flask_app


app = create_app(__name__)
# create a db
db: SQLAlchemy = SQLAlchemy(app)
if os.path.exists('/home/shashank/working/dev/projects/py/web_apps/project_viper/viper.db'):
    os.remove('/home/shashank/working/dev/projects/py/web_apps/project_viper/viper.db')
else:
    print("viper.db doesn't exist")

from tabledef import *

db.create_all()
db.app = app

os.chdir('/home/shashank/working/dev/projects/py/web_apps/project_viper')
os.system('sqlite3 viper.db < create.sql')
