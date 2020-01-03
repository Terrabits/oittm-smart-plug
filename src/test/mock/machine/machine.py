from test import create_module

# mock module `machine`
create_module('machine', 'test.mock.machine')

# relative imports workaround
nothing = None
