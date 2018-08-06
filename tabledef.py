from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = create_engine('sqlite:///viper.db', echo=True)
Base = declarative_base()


def get_sqlite_session():
    SqliteSession = sessionmaker(bind=engine)
    return SqliteSession()


id_increment = 7


def id_generator():
    global id_increment
    id_increment += 1
    return id_increment


########################################################################
class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, default=id_generator)
    username = Column(String)
    password = Column(String)
    watchlists = relationship("Watchlist")

    # ----------------------------------------------------------------------
    def __init__(self, username, password, id=None):
        """"""
        self.username = username
        self.password = password
        if id:
            self.id = id


class Watchlist(Base):
    """"""
    __tablename__ = "watchlists"

    id = Column(Integer, primary_key=True, default=id_generator)
    watchlist_items = relationship("WatchlistItem")
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    description = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, user_id, name, description, id=None):
        """"""
        self.user_id = user_id
        self.name = name
        self.description = description
        if id:
            self.id = id


class WatchlistItem(Base):
    """"""
    __tablename__ = "watchlist_items"

    id = Column(Integer, primary_key=True, default=id_generator)
    watchlist_id = Column(Integer, ForeignKey('watchlists.id'))
    symbol_id = Column(Integer, ForeignKey('symbols.id'))
    symbol = relationship("Symbol")

    # ----------------------------------------------------------------------
    def __init__(self, watchlist_id, symbol_id, id=None):
        """"""
        self.watchlist_id = watchlist_id
        self.symbol_id = symbol_id
        if id:
            self.id = id


class Symbol(Base):
    """"""
    __tablename__ = "symbols"

    id = Column(Integer, primary_key=True, default=id_generator)
    name = Column(String)
    symbol = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, name, symbol, id=None):
        """"""
        self.name = name
        self.symbol = symbol
        if id:
            self.id = id


# create tables
Base.metadata.create_all(engine)
