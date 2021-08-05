import os
import redis
import pymongo

from flasgger import Swagger
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

from ..app import app

app.config["JWT_SECRET_KEY"] = "alksdnakndsklndnlknsdn23u39204903ur9230jnf9nwndfisn"  # Change this!
jwt = JWTManager(app)

class RedisConfig:
    HOST = os.environ.get('REDIS_HOST', 'localhost')
    PORT = os.environ.get('REDIS_PORT', 6379)
    CHANNEL_NAME = 'events'
    PASSWORD = os.environ.get('REDIS_PASSWORD', '12345')

    @property
    def client(self):
        return redis.Redis(host=self.HOST, port=self.PORT, password=self.PASSWORD, db=0)


ma = Marshmallow(app)

DB_NAME = os.environ.get('MONGO_INITDB_DATABASE', 'mydatabase')
DB_USER = os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'db_user')
DB_PASSWORD = os.environ.get('MONGO_INITDB_ROOT_PASSWORD', '12345')
DB_HOST = os.environ.get('MONGO_HOST', 'localhost')
DB_PORT = os.environ.get('MONGO_PORT', '27017')
myclient = pymongo.MongoClient(f'mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?authSource=admin')
mydb = myclient["comments_db"]

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
