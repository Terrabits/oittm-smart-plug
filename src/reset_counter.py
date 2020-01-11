import machine
import time

TIME_DELTA_MS = 300
RESET_COUNT   =  10


class ResetCounter:
    def __init__(self, arg=None):
        self.last_time = time.ticks_ms()
        self.clicks    = 0

    def push(self, *args, **kwargs):
        print('ResetCounter.push')
        this_time = time.ticks_ms()
        delta     = this_time - self.last_time
        if delta <= TIME_DELTA_MS:
            self.clicks += 1
        else:
            self.clicks = 1
        self.last_time = this_time
        if self.clicks >= RESET_COUNT:
            machine.reset()
