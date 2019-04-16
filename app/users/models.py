from app import db

import peewee
import uuid
from passlib.hash import pbkdf2_sha512


class User(db.Model):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4())
    username = peewee.CharField(unique=True, max_length=50)
    password = peewee.CharField(max_length=200)

    def password_hash(self, password):
        return pbkdf2_sha512.hash(password)
