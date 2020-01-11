class MainLoopOnce:
    def __init__(self):
        self.initialized = False

    def init(self, data):
        mqtt_server = data['mqtt_server']
        smart_plug  = data['smart_plug']
        # TODO: callbacks
        def handle_mqtt_subscription(action):
            if action == 'toggle':
                smart_plug.toggle()
            elif action == 'on':
                smart_plug.on()
            elif action == 'off':
                smart_plug.off()
        mqtt_server.subscribe_callback = handle_mqtt_subscription
        smart_plug.on_toggle(mqtt_server.publish)
        mqtt_server.publish(smart_plug.state)
        self.initialized = True

    def transform(self, data):
        if not self.initialized:
            print('main_state: main/loop_once')
            self.init(data)

        # main loop
        mqtt_server = data['mqtt_server']
        mqtt_server.check_msg()
        return 'main/loop_once'
