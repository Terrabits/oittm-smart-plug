from .micropython import nothing
import micropython


# schedule function
def schedule(callback, arg):
    callback(arg)


# export
micropython.schedule = schedule

# relative imports workaround
nothing = None
