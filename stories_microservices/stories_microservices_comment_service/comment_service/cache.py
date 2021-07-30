import json

from .config.extentions import RedisConfig


class Cache(RedisConfig):

    def stringify(self, data):
        return json.dumps(data)

    def write(self, data):
        self.client.rpush('posts', self.stringify(data))
