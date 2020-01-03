import json


filename = 'state.json'

class State:
    def __init__(self):
        self._dict = dict()
        self.__getitem__ = self._dict.__getitem__
        self.__setitem__ = self._dict.__setitem__

    def save(self):
        with open(filename, 'w') as f:
            f.write(json.dumps())

    def load(self):
        pass
