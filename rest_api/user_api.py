from flask import request, jsonify
from marshmallow import fields

from data_provider import *
from rest_api.api_config import ma
from app import app
from tabledef import User

import hashlib


class PasswordField(fields.Field):
    def _serialize(self, value, attr, obj):
        hash_password = hashlib.sha224(value.encode('utf-8')).hexdigest()
        return hash_password

    def _deserialize(self, value, attr, data):
        pass


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
    password = PasswordField(attribute="password")


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/users', methods=['GET'])
def all_users():
    user_list = get_users()
    result = users_schema.jsonify(user_list)
    print("/users:", result)
    return result


@app.route('/get-user', methods=['GET'])
def user_get():
    print("request.args:", request.args)
    id = request.args["id"]
    if id:
        id = int(id)
        user = get_users(id)
        return user_schema.jsonify(user)


@app.route('/add-user', methods=['PUT'])
def user_add():
    json_request = request.get_json(silent=True)
    if json_request:
        username = json_request["username"]
        password = json_request["password"]
    if username and password:
        add_users(username=username, password=password)
        new_user = get_users(username=username)
        return user_schema.jsonify(new_user)
    else:
        return jsonify({"Error": "Either username or password weren't filled"})


@app.route('/delete-user', methods=['DELETE'])
def user_delete():
    try:
        print(request.args)
        id = request.args["id"]
        if id:
            id = int(id)
            delete_users(user_id=id)
            result = {"Status": "Deleted"}
    except Exception as e:
        print(e)
        user = get_users(user_id=id)
        if not user:
            result = {"Status": "User does not exist"}
        else:
            result = {"Status": "Something went wrong"}
    finally:
        if not result:
            result = {"Status": "Id was not passed"}

    return jsonify(result)


@app.route('/update-passwd', methods=['POST'])
def user_update():
    json_request = request.get_json(silent=True)
    id = json_request["id"]
    old_password = json_request["old_password"]
    new_password = json_request["new_password"]
    update_user(user_id=id, password=new_password)
    updated_user = get_users(user_id=id)
    return user_schema.jsonify(updated_user)
