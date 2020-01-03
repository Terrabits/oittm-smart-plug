from test import create_module

# create contents dict
contents = {
    'AP_IF': 'AP_IF',
    'STA_IF': 'STA_IF'
}

# mock module
create_module('network', 'test.mock.network', contents)

# relative imports workaround
nothing = None
