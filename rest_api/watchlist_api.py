from flask import request, jsonify

from data_provider import *
from rest_api.api_config import ma
from app import app
from tabledef import Watchlist


class WatchlistSchema(ma.ModelSchema):
    class Meta:
        model = Watchlist


watchlistSchema = WatchlistSchema(only=('name', 'description', 'id', 'user_id'))
watchlistSchemas = WatchlistSchema(many=True, only=('name', 'description', 'id', 'user_id'))


@app.route('/add-watchlist', methods=['PUT'])
def watchlist_add():
    print(request.is_json)
    print(request.get_json())
    json_request = request.get_json()
    user_id = int(json_request["user_id"])
    watchlist_name = json_request["watchlist_name"]
    watchlist_desc = json_request["watchlist_desc"]
    print("user_id:", user_id, ";watchlist_name:", watchlist_name, ";watchlist_desc:", watchlist_desc)
    add_watchlist(watchlist_name=watchlist_name, watchlist_description=watchlist_desc, user_id=user_id)
    return watchlistSchema.jsonify(get_watchlist(user_id=user_id, watchlist_name=watchlist_name))


@app.route('/delete-watchlist', methods=['DELETE'])
def watchlist_delete():
    print(request.args)
    user_id = int(request.args["user_id"])
    watchlist_id = int(request.args["watchlist_id"])
    print("user_id:", user_id, "watchlist_id:", watchlist_id)
    if get_users(user_id=user_id) and get_watchlist(watchlist_id=watchlist_id, user_id=user_id):
        print("confirmed that user and watchlist is real")
        delete_watchlist(watchlist_id=watchlist_id, user_id=user_id)
        result = jsonify({"Status": "Deleted"})
    else:
        result = jsonify({"Error": "not a real user or not a valid watchlist_id"})
    return result


@app.route('/get-watchlist', methods=['GET'])
def single_watchlist():
    print(request.args)
    user_id = request.args["user_id"]
    watchlist_id = request.args["watchlist_id"]
    if user_id and watchlist_id:
        watchlist = get_watchlist(user_id=user_id, watchlist_id=watchlist_id)
        return watchlistSchema.jsonify(watchlist)
    else:
        return jsonify({"Error": 'user_id and/or watchlist_id was not provided'})


@app.route('/watchlists', methods=['GET'])
def all_watchlists():
    print(request.args)
    user_id = request.args["user_id"]
    if user_id:
        watchlists = get_watchlist(user_id=user_id)
        return watchlistSchemas.jsonify(watchlists)
    else:
        return jsonify({"Error": "user_id was not provided"})
