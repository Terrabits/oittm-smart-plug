import machine

N = 400_000


class WifiUp:
    def __init__(self):
        self.counter = -1

    def transform(self, data):
        config = data['config']
        wifi   = data['wifi']

        if self.counter == -1:
            print('main_state: wifi/up')
            essid       = config.state['essid']
            password    = config.state['password']
            device_name = config.state['device_name']
            wifi.connect(essid, password,
                              with_hostname=device_name)
            self.counter = 0
            return 'wifi/up'
        if self.counter < N:
            if wifi.connected:
                return 'mqtt/up'
            else:
                self.counter += 1
                return 'wifi/up'

        # exceeded max count.
        if not config.state['success']:
            # assume error in config; reconfig
            config.delete()
        machine.reset()
