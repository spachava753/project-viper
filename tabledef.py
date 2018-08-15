from app import db


class User(db.Model):
    """"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    watchlists = db.relationship("Watchlist", backref='user', lazy=True)


class Watchlist(db.Model):
    """"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    watchlist_items = db.relationship("WatchlistItem", backref='watchlist')


class WatchlistItem(db.Model):
    """"""
    id = db.Column(db.Integer, primary_key=True)
    watchlist_id = db.Column(db.Integer, db.ForeignKey('watchlist.id'))
    symbol_id = db.Column(db.Integer, db.ForeignKey('symbol.id'))


class Symbol(db.Model):
    """"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    symbol = db.Column(db.String)
    watchlist_items = db.relationship("WatchlistItem", backref='symbol')
