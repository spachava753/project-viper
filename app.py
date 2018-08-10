import hashlib
import random

from flask import Flask

app = Flask(__name__)
rand_int = str(random.randint(1, 1001))
app.secret_key = hashlib.sha256(rand_int.encode()).hexdigest()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///viper.db'
app.config['SQLALCHEMY_ECHO'] = False
