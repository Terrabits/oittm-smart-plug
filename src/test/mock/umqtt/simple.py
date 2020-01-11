from   .umqtt import nothing
from   test import create_module
import umqtt


class MQTTException(Exception):
    pass


class MQTTClient:
    def __init__(self, client_id, server, keepalive=0):
        self.client_id = client_id
        self.server    = server
        self.keepalive = keepalive

        self.topics    = list()
        self.callback  = None

    def connect(self):
        return 0

    def set_callback(self, callback):
        print(f'MQTTClient.set_callback({callback})')
        self.callback = callback

    def publish(self, topic, message, *, retain=False):
        print(f'MQTTClient.publish(topic={topic}, message={message}, retain={retain})')

    def subscribe(self, topic, qos=0):
        print(f'MQTTClient.subscribe(topic={topic}, qos={qos})')
        if topic not in self.topics:
            self.topics.append(topic)

    def manually_trigger(self, topic, message):
        print(f'MQTTClient.manually_trigger(topic={topic}, message={message})')
        if topic not in self.topics:
            return
        if not self.callback:
            return
        self.callback(topic, message)

    def check_msg(self):
        raise


# place MQTTClient into umqtt.simple
create_module('umqtt.simple', 'test.mock.umqtt.simple', {'MQTTClient': MQTTClient, 'MQTTException': MQTTException})
