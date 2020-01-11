class StateMachine:
    def __init__(self):
        self.current_state = None
        self.transforms    = {}
        self.data          = {}

    def append_state(self, name, transform_fn):
        name = str(name)
        self.transforms[name] = transform_fn

    def start_at(self, name):
        name = str(name)
        self.current_state = None
        for transform_name, transform in self.transforms.items():
            if transform_name == name:
                self.current_state = name

    def loop_once(self):
        assert self.current_state, 'current state is not valid'
        self.current_state = self.transforms[self.current_state](self.data)
