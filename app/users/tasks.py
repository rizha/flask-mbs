from celery import shared_task

from .models import User


@shared_task
def total_users():
    return User.select().count()
