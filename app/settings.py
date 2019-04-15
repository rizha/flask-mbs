from environs import Env

env = Env()

REDIS_HOST = env('REDIS_HOST', 'localhost')
REDIS_PORT = env.int('REDIS_PORT', 6379)
REDIS_DB = env.int('REDIS_DB', 0)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json_formatter": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(process)d %(threadName)s "
                      "%(name)s %(levelname)s %(pathname)s"
                      " %(lineno)s %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
            "formatter": 'json_formatter'
        }
    },
    "loggers": {
        "flask.app": {
            "handlers": ['console', ],
            "propagate": False,
        }
    },
    "root": {
        "level": "ERROR",
        "handlers": ['console', ]
    }
}