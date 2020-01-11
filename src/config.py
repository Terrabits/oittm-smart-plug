import json
import os


class Config:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.state    = dict()

    def update_with(self, other):
        self.state.update(other)

    def save(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.state, f)
            return True
        except Exception:
            return False

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                self.state = json.load(f)
            return True
        except Exception:
            return False

    def clear(self):
        self.state = dict()

    def delete(self):
        self.clear()
        try:
            os.remove(self.filename)
        except Exception:
            pass
