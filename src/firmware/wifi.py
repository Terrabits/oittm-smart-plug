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
        self.access_point.config(authmode=network.AUTH_WPA2_PSK)
        self.access_point.config(password=password)

    # connect to wifi
    def connect(self, ssid, password, with_hostname='oittm-smart-plug'):
        self.access_point.active(False)
        self.station.active(True)

        self.station.config(dhcp_hostname=with_hostname)
        self.station.connect(ssid, password)

    def wait_for_station_connect(self):
        while not self.station.isconnected():
            pass

    def disconnect(self):
        self.station.disconnect()
