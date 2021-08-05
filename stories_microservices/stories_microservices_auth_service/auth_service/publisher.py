import json
from .config.extentions import RedisConf


class Publish(RedisConf):

    def __init__(self, event_type, data):
        self.sent_data = {
            'event_type': event_type,
            'data': data
        }
        try:
            self.publish()
        except:
            pass

    def stringify(self):
        return json.dumps(self.sent_data)

    def publish(self):
        self.client.publish(self.CHANNEL_NAME, self.stringify())
