import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(13,gpio.OUT)

gpio.output(13,1)

time.sleep(1)

gpio.output(13,0)

gpio.cleanup()
