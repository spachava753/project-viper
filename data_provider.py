from tabledef import get_sqlite_session, User, Watchlist, WatchlistItem, Symbol

__sqlite_session = get_sqlite_session()


def get_users():
    return __sqlite_session.query(User)


def get_user(user_filter):
    if user_filter:
        return __sqlite_session.query(User).filter(user_filter)


def get_user_watchlists(user_id):
    if user_id:
        return __sqlite_session.query(Watchlist).filter(Watchlist.user_id == user_id)


def get_watchlist_symbols(watchlist_id):
    if watchlist_id:
        symbols = []
        watchlist_items = __sqlite_session.query(WatchlistItem).filter(WatchlistItem.watchlist_id == watchlist_id)
        for watchlist_item in watchlist_items:
            symbols.append(watchlist_item.symbol.symbol)
        return symbols
