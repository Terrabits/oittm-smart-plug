from config        import Config
from http          import ConfigServer
from reset_counter import ResetCounter
from smart_plug    import SmartPlug
from wifi          import Wifi


def init_transform(data):
    print('main_state: init')
    data['config']        = Config()
    data['config_server'] = ConfigServer()
    data['mqtt_server']   = None
    data['smart_plug']    = SmartPlug()
    data['wifi']          = Wifi()

    reset_counter = ResetCounter()

    smart_plug = data['smart_plug']
    smart_plug.on_toggle(reset_counter.push)
    return 'config/load'
