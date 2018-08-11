from tabledef import User, Watchlist, WatchlistItem, Symbol
from app import db
from quote_provider import get_name_of_symbol


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


"""def get_watchlists(watchlist_id="", user_id="", watchlist_name=""):
    if watchlist_id:
        return Watchlist.query.get(watchlist_id)
    elif user_id and watchlist_name:
        return Watchlist.query.filter_by(user_id=user_id, name=watchlist_name)"""


def __commit():
    db.session.commit()


"""def delete_user_watchlists(user_id, watchlist):
    if user_id:
        sqlite_session = get_sqlite_session()
        watchlists_query = sqlite_session.query(Watchlist).filter(Watchlist.user_id == user_id,
                                                                  Watchlist.name == watchlist)
        watchlist = watchlists_query.first()
        sqlite_session.query(WatchlistItem).filter(WatchlistItem.watchlist_id == watchlist.id).delete()
        watchlists_query.delete()
        sqlite_session.commit()


def add_user_watchlists(user_id, watchlist, description):
    if user_id:
        sqlite_session = get_sqlite_session()
        if not sqlite_session.query(Watchlist).filter(Watchlist.name == watchlist).first():
            sqlite_session.add(Watchlist(user_id, watchlist, description))
            sqlite_session.commit()


def get_watchlist_symbols(watchlist_id):
    if watchlist_id:
        sqlite_session = get_sqlite_session()
        symbols = []
        watchlist_items = sqlite_session.query(WatchlistItem).filter(WatchlistItem.watchlist_id == watchlist_id)
        for watchlist_item in watchlist_items:
            if watchlist_item and watchlist_item.symbol.symbol:
                symbols.append(watchlist_item.symbol.symbol)
        return symbols


def add_watchlist_symbol(watchlist_id, symbol):
    if watchlist_id and symbol:
        symbol = symbol.upper()
        sqlite_session = get_sqlite_session()
        if __add_symbol(symbol):
            symbol = __get_symbol(symbol)
            sqlite_session.add(WatchlistItem(watchlist_id, symbol.id))
            sqlite_session.commit()


def __add_symbol(symbol):
    sqlite_session = get_sqlite_session()
    symbol_query = sqlite_session.query(Symbol).filter(Symbol.symbol == symbol).first()
    if not symbol_query and get_name_of_symbol(symbol):
        sqlite_session.add(Symbol(get_name_of_symbol(symbol), symbol))
        sqlite_session.commit()
        return True
    elif symbol_query:
        return True
    else:
        return False


def __get_symbol(symbol):
    sqlite_session = get_sqlite_session()
    return sqlite_session.query(Symbol).filter(Symbol.symbol == symbol).first()


def delete_watchlist_symbols(watchlist_id, symbols=[]):
    if watchlist_id and symbols:
        sqlite_session = get_sqlite_session()
        watchlist_items = sqlite_session.query(WatchlistItem) \
            .filter(WatchlistItem.watchlist_id == 1)

        for symbol in symbols:
            for watchlist_item in watchlist_items:
                if watchlist_item.symbol.symbol == symbol:
                    sqlite_session.query(WatchlistItem) \
                        .filter(WatchlistItem.id == watchlist_item.id) \
                        .delete()
                    break

        sqlite_session.commit()
"""