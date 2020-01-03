from types import ModuleType
from   sys import modules

def create_module(name, description, contents={}):
    modules[name] = ModuleType(name, description)
    modules[name].__dict__.update(contents)
