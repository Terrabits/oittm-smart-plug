from umqtt.simple import MQTTClient


def default_subscribe_callback(action):
    print('mqtt-subscribed action: {0}'.format(action))


# subscribe_callback(action)
# where action is 'on', 'off' or 'toggle'
class Mqtt:
    def __init__(self, name='smart-plug', main_topic='outlet',
                 subscribe_callback=default_subscribe_callback):
        # mqtt strings must be bytes
        name       = name.encode()
        main_topic = main_topic.encode()

        # device_id (name), topics, subscriptions
        self.name               = name
        self.topic              = main_topic
        self.topic_set          = main_topic + b'/set'
        self.topic_toggle       = main_topic + b'/toggle'
        self.subscribe_callback = subscribe_callback

        # start disconnected from broker
        self.address            = None
        self.broker             = None

    @property
    def connected(self):
        return bool(self.broker)

    # Attempt to connect to mqtt server at address.
    # if self.connected: will disconnect current connection before proceeding.
    # Returns True on success or False otherwise.
    def connect(self, address):
        self.disconnect()
        self.address = address
        self.broker  = MQTTClient(self.name, self.address)
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
        print('publishing state "{0}"'.format(state))
        return self.broker.publish(self.topic, state, retain=True)

    def _handle_broker_subscription(self, topic, message):
        assert self.connected, "cannot respond: disconnected"
        print('*broker subscription')
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

    # non-blocking subscription message check
    def check_msg(self):
        self.broker.check_msg()

    def loop(self):
        assert self.connected
        while 1:
            try:
                self.broker.wait_msg()
            except OSError:
                self.connect()
