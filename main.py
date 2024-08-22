import eel
import sys
from Questions import *

@eel.expose
def hello(key, var='0'):
    if key == '0': 
        value = startExecution().run(var)
        print(value)
        return value
    else:
        print('play')
        return '1'

@eel.expose
def random_python(key='0', var='0'):
    value = '0'
    print(key)
    while True:
        if value == '0':
            value = hello(key, var)

        if value == '1':
            speak('Bub bya', var)
            break

        return value

# Callback function to handle window close event
def on_close_callback(page, sockets):
    print("Window closed, exiting the application...")
    sys.exit()  # Exit the script

# Start the Eel application with a close callback
eel.start(var, close_callback=on_close_callback)