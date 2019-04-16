import os
import tempfile

import pytest

from app import create_app, init_db

@pytest.fixture
def app():
    
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(config_test=dict(
        TESTING=True,
        DATABASE=f'sqlite:///{db_path}',
        CELERY_ALWAYS_EAGER=True
    ))

    with app.app_context():
        init_db()
    
    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()