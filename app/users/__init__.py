from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from passlib.hash import pbkdf2_sha512
from werkzeug.exceptions import UnprocessableEntity



users = Blueprint('users', __name__)


class  UserSchema(Schema):
    username = fields.Str(required=True, allow_none=False)
    password = fields.Function(
            deserialize=lambda obj: pbkdf2_sha512.hash(obj),
            required=True,
        )


@users.route('/users', methods=['POST', 'GET'])
def users_resource():
    from .models import User

    if request.method == 'POST':
        try:
            payload = request.get_json() or {}
            user, _ = UserSchema(strict=True).load(payload)
            User.create(**user)
        except ValidationError as e:
            return jsonify(e.messages), UnprocessableEntity.code

        return jsonify(user), 201



__all__ = ('users',)