from test import create_module

# mock module `umqtt`
create_module('umqtt', 'test.mock.umqtt')

# relative imports workaround
nothing = None
