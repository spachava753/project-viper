from sqlalchemy.orm import sessionmaker
from tabledef import *
from flask import Flask, flash, redirect, render_template, request, session, abort
import random, hashlib, os

from app import app


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/adduser', methods=["POST"])
def add_user():
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")

    if password != confirm_password:
        return render_template("register.html")
    else:

        Session = sessionmaker(bind=engine)
        s = Session()
        user = User(username, password)
        s.add(user)
        s.commit()

        return render_template("login.html")


@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    print(result)
    if result:
        session['logged_in'] = True
        session['user_id'] = result.id
        print("user id: ", result.id)
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
