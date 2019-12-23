import network


class Wifi:
    def __init__(self):
        self.wlan  = None

    def configure_access_point(self, ssid, password, with_hostname='oittm-smart-plug'):
        self.disconnect()
        self.wlan = network.WLAN(network.AP_IF)
        self.wlan.active(True)
        self.wlan.config(essid=ssid, password=password, dhcp_hostname=with_hostname)

    def wait_for_access_point_active(self):
        while self.wlan.active() == False:
            pass

    def connect(self, ssid, password, with_hostname='oittm-smart-plug'):
        self.disconnect()
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.config(dhcp_hostname=with_hostname)
        self.wlan.connect(ssid, password)

    def wait_for_station_connect(self):
        while not self.wlan.isconnected():
            pass

    def disconnect(self):
        if not self.wlan:
            return
        self.wlan.active(False)
        self.wlan = None
