from .network import nothing
import network


class WLAN:
    def __init__(self, interface_id):
        self.interface_id = interface_id

        # defaults
        self._active      = False
        self._isconnected = False
        self._config      = dict()

    @property
    def is_access_point(self):
        return self.interface_id == network.AP_IF

    @property
    def is_station(self):
        return self.interface_id == network.STA_IF

    def active(self, set_value=None):
        if set_value == None:
            # get
            return self._active
        else:
            # set
            self._active = bool(set_value)

    def config(self, key=None, **sets):
        if key:
            # get
            return self._config.get(key)
        # set(s)
        for key, value in sets.items():
            self._config[key] = value

    def isconnected(self):
        return self._active and self._isconnected

    def connect(self, ssid=None, password=None, *, bssid=None):
        assert self.active(),   'cannot connect: inactive'
        assert self.is_station, 'cannot connect: not in STA mode'
        self._config['ssid']     = ssid
        self._config['password'] = password
        self._config['bssid']    = bssid
        self._isconnected        = True

    def disconnect(self):
        assert self.active(),   'cannot disconnect: inactive'
        assert self.is_station, 'cannot disconnect: not in STA mode'
        self._isconnected = False


# export
network.WLAN = WLAN

# relative imports workaround
nothing = None
