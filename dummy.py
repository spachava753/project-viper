import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
from tabledef import *

"""engine = create_engine('sqlite:///tutorial.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "password")
session.add(user)

# commit the record the database
session.commit()"""

sqlite_session = get_sqlite_session()

watchlist_items = sqlite_session.query(WatchlistItem) \
    .filter(WatchlistItem.watchlist_id == 1)

for watchlist_item in watchlist_items:
    if watchlist_item.symbol.symbol == 'MSFT':
        watchlist_items = sqlite_session.query(WatchlistItem) \
            .filter(WatchlistItem.id == watchlist_item.id)\
            .delete()
        break

watchlist_items = sqlite_session.query(WatchlistItem) \
    .filter(WatchlistItem.watchlist_id == 1)

for watchlist_item in watchlist_items:
    print(watchlist_item.symbol.symbol, watchlist_item.id, sep=", ")
