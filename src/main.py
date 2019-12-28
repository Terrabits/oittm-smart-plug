# import micropython
from   http import ConfigServer
import machine
from   wifi import Wifi

config_server = None
wifi          = None
wifi_config   = None


def main():
    # micropython.alloc_emergency_exception_buf(100)
    global config, config_server, wifi
    wifi = Wifi()
    wifi.configure_access_point('oittm-smart-plug', '2019hacks')

    # config
    wifi.wait_for_access_point_active()
    config_server = ConfigServer()
    config        = config_server.start()

    # connect to wifi
    essid    = config['essid']
    password = config['password']
    wifi.connect(essid, password,
                 with_hostname='oittm-smart-plug')
    wifi.wait_for_station_connect()
    if not wifi.connected:
        machine.reset()

    # turn access point off
    wifi.access_point.active(False)

    # start toggle server
    # TODO: start toggle server


if __name__ == '__main__':
    main()
