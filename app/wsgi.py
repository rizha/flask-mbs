from app import create_app, make_celery

application = create_app()
celery = make_celery(application)
