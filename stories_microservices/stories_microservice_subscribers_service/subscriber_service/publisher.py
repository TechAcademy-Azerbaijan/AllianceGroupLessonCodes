import json
from .config.extentions import RedisConfig


class Publish(RedisConfig):

    def __init__(self, event_type, data):
        self.sent_data = {
            'event_type': event_type,
            'data': data
        }
        self.publish()

    def stringify(self):
        return json.dumps(self.sent_data)

    def publish(self):
        self.client.publish(self.CHANNEL_NAME, self.stringify())
