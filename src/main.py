import micropython
from   state_machine import StateMachine
from   states        import start_transform, init_transform, config_load_transform, config_start_transform, ConfigAccessPointUp, ConfigHttpServe, config_complete_transform, run_transform, WifiUp, MqttUp, MainLoopOnce

main_state    = None


def main():
    global main_state

    main_state = StateMachine()
    main_state.append_state('start', start_transform)
    main_state.append_state('init',  init_transform)
    main_state.append_state('run',   run_transform)
    main_state.append_state('config/load',            config_load_transform)
    main_state.append_state('config/start',           config_start_transform)
    main_state.append_state('config/access_point_up', ConfigAccessPointUp().transform)
    main_state.append_state('config/serve_http',      ConfigHttpServe    ().transform)
    main_state.append_state('config/complete',        config_complete_transform)
    main_state.append_state('wifi/up', WifiUp().transform)
    main_state.append_state('mqtt/up', MqttUp().transform)
    main_state.append_state('main/loop_once', MainLoopOnce().transform)
    main_state.start_at('start')

    def loop_once_and_schedule(dummy_arg=None):
        main_state.loop_once()
        micropython.schedule(loop_once_and_schedule, None)
    loop_once_and_schedule()


if __name__ == '__main__':
    main()
