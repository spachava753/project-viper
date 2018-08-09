from flask import Flask
from flask import render_template, redirect
from flask import request, session
from flask import make_response
from quote_provider import get_all_quotes
import datetime
import random
import hashlib
from tabledef import Watchlist, User, WatchlistItem, Symbol
from data_provider import *
from app import app


@app.route('/get-watchlist', methods=['POST', 'GET'])
def get_watchlist():
    watchlists = get_user_watchlists(session['user_id'])
    print("watchlists:", watchlists)
    if session['current_watchlist']:
        print("current watchlist:", session['current_watchlist'])
        for index, watchlist in enumerate(watchlists):
            if watchlist.name == session['current_watchlist']:
                current_watchlist = watchlist
                watchlists = watchlists[:index] + watchlists[index + 1:]
                break
    else:
        current_watchlist = watchlists[0]
        watchlists = watchlists[1:]
    symbols = get_watchlist_symbols(current_watchlist.id)
    quotes = get_all_quotes(symbols)
    return render_template('home.html', current_watchlist=current_watchlist, watchlists=watchlists, quotes=quotes)


@app.route('/delete-symbol', methods=['POST'])
def delete_symbol():
    symbols = request.form.getlist('symbols')
    watchlist_name = request.form.get('watchlist-name')
    user_watchlists = get_user_watchlists(session['user_id'])
    for user_watchlist in user_watchlists:
        if user_watchlist.name == watchlist_name:
            delete_watchlist_symbols(user_watchlist.id, symbols)
            break
    return redirect('/get-watchlist', code=302)


@app.route('/add-symbol', methods=['POST'])
def add_symbol():
    symbol = request.form.get('symbol')
    watchlist_name = request.form.get('watchlist-name')
    user_watchlist = get_user_watchlists(session['user_id'], Watchlist.name == watchlist_name)
    if isinstance(user_watchlist, list):
        user_watchlist = user_watchlist[0]
    add_watchlist_symbol(user_watchlist.id, symbol)
    return redirect('/get-watchlist', code=302)


@app.route('/action-watchlist', methods=['POST', 'GET'])
def watchlist_actions():
    watchlist = request.form.get('watchlist-selected')
    if watchlist:
        if request.form.get('action') == 'Delete':
            # noinspection PyBroadException
            try:
                delete_user_watchlists(session['user_id'], watchlist)
            except Exception as e:
                print(e)
                return redirect('/login', code=302)

        elif request.form.get('action') == 'Select':
            session['current_watchlist'] = watchlist
            return redirect('/get-watchlist', code=302)

    return redirect('/', code=302)
