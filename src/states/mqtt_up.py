import machine
from   mqtt import Mqtt

MAX_TRIES = 3


class MqttUp:
    def __init__(self):
        self.counter = 0

    def transform(self, data):
        if self.counter == 0:
            print('main_state: mqtt/up')
        config = data['config']

        broker_address = config.state['broker_address']
        device_name    = config.state['device_name']
        main_topic     = config.state['main_topic']
        mqtt           = Mqtt(device_name, main_topic)
        if mqtt.connect(broker_address):
            data['mqtt_server'] = mqtt
            return 'main/loop_once'
        else:
            self.counter += 1
            if self.counter >= MAX_TRIES:
                config.delete()
                machine.reset()
