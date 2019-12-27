from umqtt.simple import MQTTClient


class Mqtt:
    def __init__(self, address, name=b'oittm', main_topic=b'smartplug', handle_on=None, handle_off=None, handle_toggle=None):
        self.name               = name
        self.topic              = main_topic
        self.topic_set          = main_topic + b'/set'
        self.topic_toggle       = main_topic + b'/toggle'

        self.address            = address
        self.broker             = None

        self.handle_on          = handle_on
        self.handle_off         = handle_off
        self.handle_toggle      = handle_toggle

    @property
    def connected(self):
        return bool(self.broker)

    def connect(self):
        self.disconnect()
        self.broker = MQTTClient(self.name, self.address, keepalive=10)
        try:
            if self.broker.connect() != 0:
                return self.connect()
            self._subscribe()
            if not self.connected:
                return self.connect()
        except OSError as err:
            print('mqtt.connect exception {0}'.format(err))
            return self.connect()
    def disconnect(self):
        if self.connected:
            try:
                self.broker.disconnect()
            except OSError as err:
                print('msqtt.disconnect exception {0}'.format(err))
        self.broker    = None
    def publish(self, state):
        assert self.connected
        try:
            return self.broker.publish(self.topic, state, retain=True, qos=1)
        except OSError:
            self.connect()
            return self.publish(state)
    def _handle_broker_subscription(self, topic, message):
        assert self.connected
        if topic == self.topic_set:
            if message == b'on':
                self.handle_on()  if self.handle_on     else None
            elif message == b'off':
                self.handle_off() if self.handle_off    else None
        elif topic == self.topic_toggle:
            self.handle_toggle() if self.handle_toggle  else None
    def _subscribe(self):
        assert self.connected
        self.broker.set_callback(self._handle_broker_subscription)
        try:
            self.broker.subscribe(self.topic_set)
            self.broker.subscribe(self.topic_toggle)
        except OSError:
            self.disconnect()
    def loop(self):
        assert self.connected
        while 1:
            try:
                self.broker.wait_msg()
            except OSError:
                self.connect()
