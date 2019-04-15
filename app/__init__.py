
import logging.config

from flask import Flask, jsonify
from werkzeug.contrib.cache import RedisCache

from app import settings

def create_app():
    logging.config.dictConfig(settings.LOGGING)
    app = Flask(__name__)

    app.config.from_object(settings)
    app.cache = RedisCache(host=settings.REDIS_HOST,
                           port=settings.REDIS_PORT,
                           db=settings.REDIS_DB)
    return app


app = create_app()

@app.route('/status')
def status():
    return jsonify(message='ok')