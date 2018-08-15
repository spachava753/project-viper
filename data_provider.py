from tabledef import *
from app import db
from quote_provider import get_name_of_symbol


# User crud operations

def get_users(user_id="", username=""):
    if user_id:
        return User.query.get(user_id)
    elif username:
        return User.query.filter_by(username=username).first()

    return User.query.all()


def add_users(username, password):
    if username and password:
        db.session.add(User(username=username, password=password))
        __commit()
    else:
        raise Exception('Username nor password not was a valid input')


def delete_users(username="", user_id=""):
    if user_id and get_users(user_id=user_id):
        db.session.delete(get_users(user_id=user_id))
    elif username and get_users(username=username):
        db.session.delete(get_users(username=username))
    else:
        raise Exception('Neither username nor user id not was a valid input')

    __commit()


def update_user(user_id, username="", password=""):
    if user_id and get_users(user_id=user_id):
        user = get_users(user_id=user_id)
        if username:
            user.username = username
        if password:
            user.password = password
        db.session.add(user)
        __commit()
    else:
        raise Exception('Neither username nor user id not was a valid input')


# Watchlist crud operations

def get_watchlist(watchlist_id="", user_id="", watchlist_name=""):
    if watchlist_id:
        return Watchlist.query.get(watchlist_id)
    elif user_id and watchlist_name:
        return Watchlist.query.filter_by(user_id=user_id, name=watchlist_name).first()
    elif user_id:
        return Watchlist.query.filter_by(user_id=user_id).all()
    else:
        raise Exception('Neither username nor user id not was a valid input')


def add_watchlist(watchlist_name, watchlist_description, user_id):
    if watchlist_name and watchlist_description and user_id:
        if not get_watchlist(user_id=user_id, watchlist_name=watchlist_name):
            user = get_users(user_id=user_id)
            watchlist = Watchlist(user_id=user_id, description=watchlist_description, name=watchlist_name, user=user)
            db.session.add(watchlist)
            __commit()
    else:
        raise Exception('Neither username nor user id not was a valid input')


def delete_watchlist(watchlist_name="", user_id="", watchlist_id=""):
    if watchlist_id:
        db.session.delete(get_watchlist(watchlist_id=watchlist_id))
    elif watchlist_name and user_id:
        db.session.delete(get_watchlist(user_id=user_id, watchlist_name=watchlist_name))
    else:
        raise Exception('No params were supplied')


# Watchlist_item CRUD operations
def add_watchlist_symbol(watchlist_id, symbol):
    if watchlist_id:
        try:
            watchlist = Watchlist.query.filter_by(id=watchlist_id).first()
            symbol = __get_symbol(symbol)
            watchlist_item = WatchlistItem(watchlist=watchlist, symbol=symbol)
            db.session.add(watchlist_item)
            __commit()
        except Exception as e:
            print(e)
        finally:
            db.session.rollback()


def delete_watchlist_symbol(watchlist_id, symbol):
    if watchlist_id:
        try:
            watchlist = Watchlist.query.filter_by(id=watchlist_id).first()
            symbol = __get_symbol(symbol)
            watchlist_item = WatchlistItem(watchlist=watchlist, symbol=symbol)
            watchlist_item.delete()
            __commit()
        except Exception as e:
            print(e)
        finally:
            db.session.rollback()


def get_watchlist_symbols(watchlist_id):
    if watchlist_id:
        return WatchlistItem.query.filter_by(watchlist_id=watchlist_id).all()


def __get_symbol(symbol):
    # check if real symbol
    symbol = symbol.upper()
    if symbol and get_name_of_symbol(symbol):
        symbol_query = Symbol.query.filter_by(name=get_name_of_symbol(symbol))
        if symbol_query:
            return symbol_query.first()
        else:
            __add_symbol(symbol)
            return __get_symbol(symbol)
    else:
        msg = "{} is not a real symbol".format(symbol.upper())
        raise Exception(msg)


def __add_symbol(symbol):
    # check if real symbol
    symbol = symbol.upper()
    if symbol and get_name_of_symbol(symbol):
        symbol = Symbol(name=get_name_of_symbol(symbol), symbol=symbol)
        db.session.add(symbol)
        __commit()


def __commit():
    db.session.commit()
