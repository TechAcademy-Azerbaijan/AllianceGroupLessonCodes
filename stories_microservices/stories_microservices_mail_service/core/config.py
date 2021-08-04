import os
import redis


class RedisConfig:
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    CHANNEL_NAME = 'events'
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '12345')

    @classmethod
    def client(cls):
        return redis.Redis(host=cls.REDIS_HOST, port=cls.REDIS_PORT, password=cls.REDIS_PASSWORD, db=0)


class EmailConfig:
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'idris.sabanli@gmail.com'
    EMAIL_HOST_PASSWORD = 'tmuoqqazogwupsna'