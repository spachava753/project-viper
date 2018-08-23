from data_provider import *
from rest_api.api_config import ma
from app import app


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/users', methods=['GET'])
def all_users():
    user_list = get_users()
    result = users_schema.jsonify(user_list)
    print("/users:", result)
    return result
