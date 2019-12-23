class Mutex:
    def __init__(self):
        self.unlock()

    def __enter__(self):
        self.lock()

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
            return
        self.unlock()

    @property
    def locked(self):
        return self.state == 'locked'

    @property
    def unlocked(self):
        return self.state == 'unlocked'

    def lock(self):
        self.state = 'locked'

    def unlock(self):
        self.state = 'unlocked'
