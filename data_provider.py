from tabledef import User, Watchlist, WatchlistItem, Symbol, db
from quote_provider import get_name_of_symbol


def get_users():
    sqlite_session = get_sqlite_session()
    return sqlite_session.query(User)


def get_user(user_filter):
    if user_filter:
        sqlite_session = get_sqlite_session()
        return sqlite_session.query(User).filter(user_filter)


def get_user_watchlists(user_id, watchlist_filter=""):
    if user_id:
        sqlite_session = get_sqlite_session()
        if watchlist_filter:
            watchlist_query = sqlite_session.query(Watchlist).filter(Watchlist.user_id == user_id,
                                                                     Watchlist.name == watchlist_filter)
        else:
            watchlist_query = sqlite_session.query(Watchlist).filter(Watchlist.user_id == user_id)
        return watchlist_query.all()


def delete_user_watchlists(user_id, watchlist):
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
