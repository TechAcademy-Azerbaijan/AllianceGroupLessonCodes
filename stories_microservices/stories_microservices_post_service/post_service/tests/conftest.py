import os

import flask_migrate
import pytest
from ..app import app as flask_app
from ..config.extentions import PROJECT_DIR


@pytest.fixture
def client():
    DB_PATH = os.path.join(PROJECT_DIR, 'test.db')
    with flask_app.app_context():
        flask_app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{DB_PATH}"
        # flask_migrate.init(directory='test_migrations', multidb=False)
        # flask_migrate.migrate(directory='test_migrations', message=None, sql=False, head='head', splice=False, branch_label=None, version_path=None, rev_id=None)
        flask_migrate.upgrade(directory='test_migrations', revision='head', sql=False, tag=None)
    return flask_app.test_client()


