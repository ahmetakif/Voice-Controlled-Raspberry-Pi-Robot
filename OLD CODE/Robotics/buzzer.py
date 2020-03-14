
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(21,gpio.OUT)

gpio.output(21,1)

time.sleep(0.1)

gpio.output(21,0)

time.sleep(0.1)

gpio.output(21,1)

time.sleep(0.1)

gpio.output(21,0)

time.sleep(0.1)

gpio.output(21,1)

time.sleep(0.1)

gpio.output(21,0)

gpio.cleanup()
