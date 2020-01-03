from umqtt.simple import MQTTClient


def default_subscribe_callback(action):
    print('mqtt-subscribed action: {0}'.format(action))


# subscribe_callback(action)
# where action is 'on', 'off' or 'toggle'
class Mqtt:
    def __init__(self, address,
                 name=b'smart-plug', main_topic=b'outlet',
                 subscribe_callback=default_subscribe_callback):
        self.address            = address
        self.name               = name
        self.topic              = main_topic
        self.topic_set          = main_topic + b'/set'
        self.topic_toggle       = main_topic + b'/toggle'
        self.broker             = None
        self.subscribe_callback = subscribe_callback

    @property
    def connected(self):
        return bool(self.broker)

    # Attempt to connect to mqtt server.
    # if self.connected: will disconnect current connection before proceeding.
    # Returns True on success or False otherwise.
    def connect(self):
        self.disconnect()
        self.broker = MQTTClient(self.name, self.address, keepalive=10)
        if self.broker.connect() != 0:
            # failed
            self.broker = None
            return False
        # succeeded
        self.broker.set_callback(self._handle_broker_subscription)
        self.broker.subscribe(self.topic_set)
        self.broker.subscribe(self.topic_toggle)
        return True

    def disconnect(self):
        if not self.connected:
            return
        self.broker.disconnect()
        self.broker = None

    def publish(self, state):
        assert self.connected, "cannot publish: disconnected."
        return self.broker.publish(self.topic, state, retain=True, qos=1)

    def _handle_broker_subscription(self, topic, message):
        assert self.connected, "cannot respond: disconnected"
        if topic == self.topic_set:
            if message == b'on':
                self.subscribe_callback('on')
            elif message == b'off':
                self.subscribe_callback('off')
            else:
                # unrecognized message
                pass
        elif topic == self.topic_toggle:
            self.subscribe_callback('toggle')
        else:
            # unrecognized topic
            pass

    def loop(self):
        assert self.connected
        while 1:
            try:
                self.broker.wait_msg()
            except OSError:
                self.connect()
