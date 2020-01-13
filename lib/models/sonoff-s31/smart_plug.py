from machine import Pin
from mutex   import Mutex


class SmartPlug(object):
    def __init__(self):
        self.mutex            = Mutex()
        self.toggle_callbacks = []

        self.state  = None
        self.led    = Pin(13, Pin.OUT)  # active low
        self.relay  = Pin(12, Pin.OUT)
        self.button = Pin( 0, Pin.IN )

        self.led.off() # always on
        self.off()

        def button_callback():
            print('*button pressed')
            self.toggle()
        self.set_button_callback(button_callback)

    def on(self):
        if self.mutex.locked:
            return
        if self.state == 'on':
            return
        with self.mutex:
            print('smart plug on')
            self.state = 'on'
            self.relay.on()
        self.notify_toggle_observers()

    def off(self):
        if self.state == 'off':
            return
        if self.mutex.locked:
            return
        with self.mutex:
            print('smart plug off')
            self.state = 'off'
            self.relay.off()
        self.notify_toggle_observers()

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
        def callback_ignore_input(pin_number):
            callback()
        self.button.irq(trigger=trigger, handler=callback_ignore_input)

    def push_button(self):
        self.button_callback()
