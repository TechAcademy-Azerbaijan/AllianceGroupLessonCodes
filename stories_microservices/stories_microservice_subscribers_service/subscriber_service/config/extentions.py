import os
import redis
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flasgger import Swagger

from .base import Config, RedisConfig
from ..app import app

app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
ma = Marshmallow(app)
swagger = Swagger(app)


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
