from flask import Blueprint, request, jsonify, current_app
from marshmallow import Schema, fields, ValidationError
import peewee


from .models import User

users = Blueprint('users', __name__)


class UserSchema(Schema):
    username = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)


@users.route('/users', methods=['POST', 'GET'])
def users_resource():
    if request.method == 'POST':
        try:
            payload = request.get_json() or {}
            user, _ = UserSchema(strict=True).load(payload)

            user['password'] = User().password_hash(user['password'])
            User.create(**user)

        except ValidationError as e:
            return jsonify(e.messages), 422

        except peewee.IntegrityError as e:
            if 'unique' in repr(e).lower():
                return jsonify(messages='Username already exists'), 409

        return jsonify(user), 201

    elif request.method == 'GET':
        users = []
        for user in User.select():
            users.append(dict(
                id=user.id,
                username=user.username,
                password=user.password
            ))
        return jsonify(users)


@users.route('/users/login', methods=['POST',])
def login():
    from werkzeug.exceptions import Unauthorized
    try:
        payload = request.get_json() or {}
        auth_data, _ = UserSchema(strict=True).load(payload)
        user = User.get(username=auth_data['username'])

        if not user.verify_password(auth_data['password']):
            raise Unauthorized

    except ValidationError as e:
        return jsonify(e.messages), 422

    except (User.DoesNotExist, Unauthorized):
        return jsonify(message='Invalid Username or Password'), 401

    return jsonify(token=user.token), 201