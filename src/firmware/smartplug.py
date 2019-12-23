from machine import Pin
from mutex   import Mutex


class SmartPlug(object):
    def __init__(self):
        self.mutex            = Mutex()
        self.toggle_callbacks = []
        self.button_callback  = None

        self.state  = None
        self.led    = Pin(13, Pin.OUT)  # active low
        self.relay  = Pin( 4, Pin.OUT)
        self.button = Pin(12, Pin.IN )
        self.set_button_callback(self.toggle)
        self.off()

    def on(self):
        if self.mutex.locked:
            return
        if self.state == 'on':
            return
        with self.mutex:
            self.state = 'on'
            self.led.off()
            self.relay.on()
        self.notify_observers()

    def off(self):
        if self.state == 'off':
            return
        if self.mutex.locked:
            return
        with self.mutex:
            self.state = 'off'
            self.led.on()
            self.relay.off()
        self.notify_observers()

    def toggle(self):
        if self.state == 'on':
            self.off()
        else:
            self.on()

    # observer pattern for toggle
    def on_toggle(self, callback):
        self.toggle_callbacks.append(callback)

    def notify_toggle_observers(self):
        for callback in self.toggle_callbacks:
            callback(self.state)

    # push button
    def set_button_callback(self, callback, trigger=Pin.IRQ_RISING):
        self.button_callback = callback

        def callback_ignore_input(i):
            callback()
        self.button.irq(trigger=trigger, handler=callback_ignore_input)

    def push_button(self):
        if not self.button_callback:
            return
        self.button_callback()
