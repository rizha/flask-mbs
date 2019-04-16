import importlib
import logging.config

import click
from flask import Flask, jsonify
from flask.cli import with_appcontext
from werkzeug.contrib.cache import RedisCache
from playhouse.flask_utils import FlaskDB
from celery import Celery

from app import settings

db = FlaskDB()


def create_app(config_test=None):
    logging.config.dictConfig(settings.LOGGING)
    app = Flask(__name__)
    app.config.from_object(settings)

    if config_test:
        app.config.update(config_test)

    db.init_app(app)

    app.db = db

    app.cache = RedisCache(host=settings.REDIS_HOST,
                           port=settings.REDIS_PORT,
                           db=settings.REDIS_DB)

    for module, bp in settings.APPS:
        module = importlib.import_module(module)
        app.register_blueprint(getattr(module, bp))

    @app.shell_context_processor
    def make_shell_context():
        return dict(app=app, db=db)

    @app.route('/status')
    def status():
        app.logger.info("hi i'm logging GET /status route")
        return jsonify(message='ok')

    @click.command('init_db')
    @with_appcontext
    def init_db_command():
        """Create new tables."""
        init_db()
        click.echo('Initialize the tables')

    app.cli.add_command(init_db_command)

    return app


def init_db():
    from app.users.models import User
    with db.database:
        db.database.create_tables([User, ])


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'],
        CELERY_ALWAYS_EAGER=True
    )
    celery.conf.update(app.config)
    celery.autodiscover_tasks([apps[0]
                               for apps in app.config['APPS']], force=True)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
