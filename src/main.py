# import micropython
from   http      import ConfigServer
import machine
from   smartplug import SmartPlug
from   wifi      import Wifi

config        = None
config_server = None
smart_plug    = None
wifi          = None


def main():
    # micropython.alloc_emergency_exception_buf(100)
    global config, config_server, smart_plug, wifi
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

    # initialize smart plug control
    smart_plug = SmartPlug()

if __name__ == '__main__':
    main()
