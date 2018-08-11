from app import db


class User(db.Model):
    """"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    watchlists = db.relationship("Watchlist")


class Watchlist(db.Model):
    """"""
    __tablename__ = "watchlists"

    id = db.Column(db.Integer, primary_key=True)
    watchlist_items = db.relationship("WatchlistItem")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String)
    description = db.Column(db.String)


class WatchlistItem(db.Model):
    """"""
    __tablename__ = "watchlist_items"

    id = db.Column(db.Integer, primary_key=True)
    watchlist_id = db.Column(db.Integer, db.ForeignKey('watchlists.id'))
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbols.id'))
    symbol = db.relationship("Symbol")


class Symbol(db.Model):
    """"""
    __tablename__ = "symbols"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    symbol = db.Column(db.String)
