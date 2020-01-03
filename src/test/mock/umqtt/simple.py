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
        print('MQTTClient.set_callback({0})'.format(callback))
        self.callback = callback

    def subscribe(self, topic, qos=0):
        print('MQTTClient.subscribe(topic={topic}, qos={qos})'.format(topic=topic, qos=qos))
        if topic not in self.topics:
            self.topics.append(topic)

    def manually_trigger(self, topic, message):
        if topic not in self.topics:
            return
        if not self.callback:
            return
        self.callback(topic, message)


# place MQTTClient into umqtt.simple
create_module('umqtt.simple', 'test.mock.umqtt.simple', {'MQTTClient': MQTTClient, 'MQTTException': MQTTException})
