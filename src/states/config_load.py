def config_load_transform(data):
    print('main_state: config/load')
    if data['config'].load():
        return 'run'
    else:
        return 'config/start'
