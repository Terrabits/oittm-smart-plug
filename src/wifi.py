import network


class Wifi:
    def __init__(self):
        self.station      = network.WLAN(network.STA_IF)
        self.access_point = network.WLAN(network.AP_IF)

    def configure_access_point(self, essid, password):
        self.station.active(False)
        self.access_point.active(True)

        # config
        self.access_point.config(essid=essid)
        self.access_point.config(password=password)
        # self.access_point.config(authmode=network.AUTH_WPA2_PSK)

    def wait_for_access_point_active(self):
        while not self.access_point.active():
            pass

    # connect to wifi
    def connect(self, ssid, password, with_hostname='oittm-smart-plug'):
        self.station.active(True)
        self.station.config(dhcp_hostname=with_hostname)
        self.station.connect(ssid, password)

    @property
    def connected(self):
        return self.station.isconnected()

    def wait_for_station_connect(self):
        i = 100000
        while not self.connected:
            i -= 1
            if i <= 0:
                break

    def disconnect(self):
        self.station.disconnect()
