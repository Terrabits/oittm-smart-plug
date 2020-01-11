# # This file is executed on every boot (including wake-boot from deepsleep)
# #import esp
# #esp.osdebug(None)
import uos, machine
# #uos.dupterm(None, 1) # disable REPL on UART(0)
# import gc
# #import webrepl
# #webrepl.start()
# gc.collect()

import gc
import micropython


# set aside 100 bytes for exceptions
micropython.alloc_emergency_exception_buf(100)

# collect garbage
gc.collect()
