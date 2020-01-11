# OITTM Smart Plug Hack

Yet another ESP8266-based smart plug hack.

The smart plug starts in access point mode and serves the following pages via HTTP:

![Configure form](doc/screenshots/post-config.png)

![Configure confirmation page](doc/screenshots/display-config.png)

Once the configuration information is submitted, the smart plug will restart and attempt to connect to wifi and the mqtt broker. If successful, it will continue to function. If unsuccessful, it will restart in access point mode and you can try again.

Pushing the button 10 times quickly (< 3 s) will cause the smart plug to reboot.

Said another way:

![state machine](doc/screenshots/main-state-machine.png)
