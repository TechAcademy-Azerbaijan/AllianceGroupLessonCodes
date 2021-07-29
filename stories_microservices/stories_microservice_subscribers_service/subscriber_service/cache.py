import json

from .config.extentions import RedisConfig


class Cache(RedisConfig):

    def stringify(self, data):
        return json.dumps(data)

    def write(self, data):
        self.client.rpush('posts', self.stringify(data))

    def load(self, data_list):
        return map(lambda data: json.loads(data), data_list)

    def read(self):
        return self.load(data_list=self.client.lrange('posts', 0, -1))
