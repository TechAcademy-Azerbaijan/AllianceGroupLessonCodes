import json
from ast import literal_eval

from .config.extentions import RedisConfig


class Cache(RedisConfig):

    def stringify(self, data):
        return json.dumps(data)

    def write(self, data):
        self.client.rpush('posts', self.stringify(data))

    def load(self, data_list):
        json_data = []
        for data in data_list:
            json_data.append(json.loads(json.loads(data.decode('utf8'))))
        return json_data

    def read(self):
        data = self.load(data_list=self.client.lrange('posts', 0, -1))
        self.client.delete('posts')
        return data
