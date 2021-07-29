import os
import redis
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from ..app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://db_user:12345@localhost:5434/db_name"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['CELERY_BROKER_URL'] = "redis://:12345@localhost:6379/0"


class RedisConfig:
    HOST = os.environ.get('REDIS_HOST', 'localhost')
    PORT = os.environ.get('REDIS_PORT', 6379)
    CHANNEL_NAME = 'events'
    PASSWORD = os.environ.get('REDIS_PASSWORD', '12345')

    @property
    def client(self):
        return redis.Redis(host=self.HOST, port=self.PORT, password=self.PASSWORD, db=0)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
ma = Marshmallow(app)
swagger = Swagger(app)


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
