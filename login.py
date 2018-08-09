from sqlalchemy.orm import sessionmaker
from tabledef import *
from flask import Flask, flash, redirect, render_template, session, request, abort
import random, hashlib, os
from data_provider import *
from quote_provider import get_all_quotes

from app import app


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        watchlists = get_user_watchlists(session['user_id'])
        print("watchlists length: ", watchlists)
        current_watchlist = watchlists[0]
        watchlists = watchlists[1:]
        symbols = get_watchlist_symbols(current_watchlist.id)
        print(symbols)
        quotes = get_all_quotes(symbols)
        print(quotes)
        return render_template('home.html', current_watchlist=current_watchlist, watchlists=watchlists, quotes=quotes)


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
        s = get_sqlite_session()
        user = User(username, password)
        s.add(user)
        s.commit()

        return render_template("login.html")


@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
    POST_USERNAME = ""
    POST_PASSWORD = ""
    try:
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
    except Exception as e:
        print(e)
    finally:
        if not POST_PASSWORD or not POST_USERNAME:
            return home()
        s = get_sqlite_session()
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
