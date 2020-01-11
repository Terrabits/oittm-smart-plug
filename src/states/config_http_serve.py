class ConfigHttpServe:
    def __init__(self):
        self.started = False

    def transform(self, data):
        config        = data['config']
        config_server = data['config_server']

        if not self.started:
            print('main_state: config/serve_http')
            config_server.start()
            self.started = True
            return 'config/serve_http'

        post_result = config_server.loop_once()
        if post_result:
            config.update_with(post_result)
            config.state['success'] = False
            config.save()
            return 'config/complete'

        # keep serving
        return 'config/serve_http'
