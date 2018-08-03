from sqlalchemy.orm import sessionmaker
from tabledef import *
from flask import Flask, flash, redirect, render_template, request, session, abort
import random
import hashlib


engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"


@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    rand_int = str(random.randint(1, 1001))
    app.secret_key = hashlib.sha256(rand_int.encode()).hexdigest()
    app.run(port=8080, debug=True, host='0.0.0.0')
