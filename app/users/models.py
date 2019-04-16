from app import db

import peewee
import uuid


class User(db.Model):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4())
    username = peewee.CharField(unique=True, max_length=50)
    password = peewee.CharField(max_length=200)
