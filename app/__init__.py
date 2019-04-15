
import logging.config

from flask import Flask, jsonify, current_app
from playhouse.flask_utils import FlaskDB
from werkzeug.contrib.cache import RedisCache

from app import settings


def create_app(config_test=None):
    logging.config.dictConfig(settings.LOGGING)
    app = Flask(__name__)
    app.config.from_object(settings)
    
    if config_test:
        app.config.update(config_test)
    
    db = FlaskDB(app)
    app.db = db

    app.cache = RedisCache(host=settings.REDIS_HOST,
                           port=settings.REDIS_PORT,
                           db=settings.REDIS_DB)
    
    from app.users import users
    app.register_blueprint(users)
    
    @app.shell_context_processor
    def make_shell_context():
        return dict(app=app, db=db)


    @app.route('/status')
    def status():
        app.logger.info("hi i'm logging GET /status route")
        return jsonify(message='ok')

    return app


def init_db():
    from app.users.models import User
    with current_app.app_context():
        current_app.db.database.create_tables([User,])