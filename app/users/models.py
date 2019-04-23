import uuid
from datetime import timedelta, datetime

import peewee
import jwt
from passlib.hash import pbkdf2_sha512

from app import settings
from app import db



class User(db.Model):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4())
    username = peewee.CharField(unique=True, max_length=50)
    password = peewee.CharField(max_length=200)

    def password_hash(self, password):
        return pbkdf2_sha512.hash(password)
    
    def verify_password(self, password):
        return pbkdf2_sha512.verify(password, self.password)

    @property
    def token(self):
        expiry = datetime.now() + timedelta(seconds=settings.TOKEN_EXPIRY)
        return jwt.encode({'exp': expiry},
            settings.SECRET_KEY, algorithm='HS256').decode()