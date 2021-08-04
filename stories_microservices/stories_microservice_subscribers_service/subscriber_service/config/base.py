import os
from datetime import timedelta

import redis


class RedisConfig:
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    CHANNEL_NAME = 'events'
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '12345')

    @property
    def client(self):
        return redis.Redis(host=self.REDIS_HOST, port=self.REDIS_PORT, password=self.REDIS_PASSWORD, db=0)


class Config:
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'db_user')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'db_name')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '12345')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5434')
    SQLALCHEMY_DATABASE_URI = f"postgresql://" \
                              f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "12345"
    SECURITY_PASSWORD_SALT = '12345'
    JWT_SECRET_KEY = 'alksdnakndsklndnlknsdn23u39204903ur9230jnf9nwndfisn'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    CELERY_BROKER_URL = f"redis://:{RedisConfig.REDIS_PASSWORD}@{RedisConfig.REDIS_HOST}:{RedisConfig.REDIS_PORT}/0"
