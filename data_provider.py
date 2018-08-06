from tabledef import get_sqlite_session, User, Watchlist, WatchlistItem, Symbol


def get_users():
    __sqlite_session = get_sqlite_session()
    return __sqlite_session.query(User)


def get_user(user_filter):
    if user_filter:
        __sqlite_session = get_sqlite_session()
        return __sqlite_session.query(User).filter(user_filter)


def get_user_watchlists(user_id, watchlist_filter=""):
    if user_id:
        __sqlite_session = get_sqlite_session()
        if watchlist_filter:
            return __sqlite_session.query(Watchlist).filter(Watchlist.user_id == user_id, watchlist_filter)
        else:
            return __sqlite_session.query(Watchlist).filter(Watchlist.user_id == user_id)


def delete_user_watchlists(user_id, watchlist):
    if user_id:
        __sqlite_session = get_sqlite_session()
        __sqlite_session.query(Watchlist).filter(Watchlist.user_id == user_id and Watchlist.name == watchlist).delete()
        __sqlite_session.commit()


def get_watchlist_symbols(watchlist_id):
    if watchlist_id:
        __sqlite_session = get_sqlite_session()
        symbols = []
        watchlist_items = __sqlite_session.query(WatchlistItem).filter(WatchlistItem.watchlist_id == watchlist_id)
        for watchlist_item in watchlist_items:
            if watchlist_item and watchlist_item.symbol.symbol:
                symbols.append(watchlist_item.symbol.symbol)
        return symbols


def add_watchlist_symbol(watchlist_id, symbol):
    if watchlist_id:
        __sqlite_session = get_sqlite_session()
        symbol_query = __sqlite_session.query(Symbol).filter(Symbol.symbol == symbol).first()
        __sqlite_session.add(WatchlistItem(watchlist_id, symbol_query.id))
        __sqlite_session.commit()
        __sqlite_session.flush()


def delete_watchlist_symbols(watchlist_id, symbols=[]):
    if watchlist_id and symbols:
        __sqlite_session = get_sqlite_session()
        watchlist_items = __sqlite_session.query(WatchlistItem) \
            .filter(WatchlistItem.watchlist_id == 1)

        for symbol in symbols:
            for watchlist_item in watchlist_items:
                if watchlist_item.symbol.symbol == symbol:
                    __sqlite_session.query(WatchlistItem) \
                        .filter(WatchlistItem.id == watchlist_item.id) \
                        .delete()
                    break

        __sqlite_session.commit()
