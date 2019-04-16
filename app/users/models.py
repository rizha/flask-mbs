from app import current_app

import peewee
import uuid



db = current_app.db


class User(peewee.Model):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4())
    username = peewee.CharField(unique=True, max_length=50)
    password = peewee.CharField(max_length=200)

    class Meta:
        database = db