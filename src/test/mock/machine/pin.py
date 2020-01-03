from .machine import nothing
import machine


class Pin:
    # direction
    IN          = 'in'
    OUT         = 'out'

    # triggers
    IRQ_FALLING = 2**0
    IRQ_RISING  = 2**1

    def __init__(self, no, dir=IN):
        self.state      = None
        self.pin_number = no
        self.direction  = dir
        self.button_callback = None

    def __str__(self):
        return '<Pin pin_number={pin_number} direction={direction} state={state}>'.format(pin_number=self.pin_number, direction=self.direction, state=self.state)

    def __repr__(self):
        return str(self)

    def on(self):
        if self.state == 'on':
            return
        self.state = 'on'
        print(self)

    def off(self):
        if self.state == 'off':
            return
        self.state = 'off'
        print(self)

    def irq(self, handler=None, trigger=IRQ_FALLING | IRQ_RISING, hard=False):
        self.button_callback = handler
        self.trigger = trigger
        self.hard    = hard


# replace original
machine.Pin = Pin

# relative imports workaround
nothing = None
