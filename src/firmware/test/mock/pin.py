import machine


class Pin(object):
    IN         = 'in'
    OUT        = 'out'
    IRQ_RISING = 'irq_rising'

    def __init__(self, index, io):
        self.state = None
        self.index = index
        self.io    = io
        self.button_callback = None

    def __str__(self):
        return '<Pin index={index} io={io} state={state}>'.format(index=self.index, io=self.io, state=self.state)

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


# replace original
machine.Pin = Pin

# relative imports workaround
nothing = None
