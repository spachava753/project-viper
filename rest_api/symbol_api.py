from flask import request, jsonify
from marshmallow import fields, Schema

from data_provider import *
from rest_api.api_config import ma
from app import app
from tabledef import WatchlistItem, Symbol


class WatchlistSymbol(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            raise Exception("No value in serialization method")
        print("value is:", value)
        symbol = get_symbol(symbol_id=value).symbol
        return symbol

    def _deserialize(self, value, attr, data):
        pass


class WatchlistItemSchema(ma.ModelSchema):
    class Meta:
        model = WatchlistItem

    symbol = WatchlistSymbol(attribute="symbol_id")


watchlist_item_schema = WatchlistItemSchema(many=True)


@app.route('/symbols', methods=['GET'])
def all_symbols():
    print(request.args)
    watchlist_id = int(request.args['watchlist_id'])
    watchlist_items = get_watchlist_symbols(watchlist_id=watchlist_id)
    result = watchlist_item_schema.jsonify(watchlist_items)
    print(result)
    return result


@app.route('/add-symbol', methods=['PUT'])
def symbol_add():
    print(request.args)
    watchlist_id = int(request.args['watchlist_id'])
    watchlist_items = get_watchlist_symbols(watchlist_id=watchlist_id)
    result = watchlist_item_schema.jsonify(watchlist_items)
    print(result)
    return result


@app.route('/delete-symbol', methods=['DELETE'])
def symbol_delete():
    pass
