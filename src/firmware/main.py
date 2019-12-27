# import micropython
from   http import ConfigServer
from   wifi import Wifi

config_server = None
wifi          = None
wifi_config   = None


def main():
    # micropython.alloc_emergency_exception_buf(100)
    global config, config_server, wifi
    wifi = Wifi()
    wifi.configure_access_point('oittm-smart-plug', '2019hacks')
    config_server = ConfigServer()

    # config
    wifi.wait_for_access_point_active()
    config = config_server.start()

    # connect to wifi
    essid    = config['essid']
    password = config['password']
    wifi.connect(essid, password,
                 with_hostname='oittm-smart-plug')


if __name__ == '__main__':
    main()
