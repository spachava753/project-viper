from tabledef import *
from flask import Flask
import random, hashlib, os

if not os.path.exists('viper.db'):
    import tabledef
app = Flask(__name__)
rand_int = str(random.randint(1, 1001))
app.secret_key = hashlib.sha256(rand_int.encode()).hexdigest()