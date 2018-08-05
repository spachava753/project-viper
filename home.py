from flask import Flask
from flask import render_template
from flask import request, session
from flask import make_response
from quote_provider import get_all_quotes
import datetime
import random
import hashlib
from tabledef import Watchlist, User, WatchlistItem, Symbol
from app import app


@app.route('/get-watchlist', methods=['POST'])
def get_watchlist():
    watchlists = session.get(Watchlist).filter(Watchlist.user_id == session['user_id'])
    print("watchlists: ", watchlists)
    if watchlists:
        current_watchlist = watchlists[0].name
    watchlists = watchlists[1:]
    return render_template("home.html", current_watchlist=current_watchlist, watchlists=watchlists)
