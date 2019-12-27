# import micropython
from   http import ConfigServer
from   wifi import Wifi

config_server = None
wifi          = None


def main():
    # micropython.alloc_emergency_exception_buf(100)
    # TODO: main code goes here
    global config_server, wifi
    wifi = Wifi()
    wifi.configure_access_point('oittm-smart-plug', '2019hacks')
    config_server = ConfigServer()

    # start
    wifi.wait_for_access_point_active()
    config_server.start()


if __name__ == '__main__':
    main()
