import machine

N = 400_000


class ConfigAccessPointUp:
    def __init__(self):
        self.counter = -1

    def transform(self, data):
        wifi = data['wifi']
        if self.counter == -1:
            print('main_state: config/access_point_up')
            wifi.configure_access_point('smart-plug-config', '2020hacks2020')
            self.counter = 0
            return 'config/access_point_up'
        if self.counter < N:
            if wifi.access_point.active():
                self.counter = -1
                return 'config/serve_http'
            else:
                self.counter += 1
                return 'config/access_point_up'

        # loop limit. reset and retry.
        machine.reset()
