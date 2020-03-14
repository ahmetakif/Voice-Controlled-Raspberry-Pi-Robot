import RPi.GPIO as gpio
import time

gpio.setwarnings(False)

dir = 21
step = 20

def init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(dir,gpio.OUT)
    gpio.setup(step,gpio.OUT)
    gpio.output(dir,0)
    gpio.output(step,0)

def ileri(tf,sf):
    init()
    gpio.output(dir,1)
    gpio.output(step,0)
    ip = gpio.PWM(step,sf)
    ip.start(50)
    time.sleep(tf)
    gpio.cleanup()

def geri(tf,sf):
    init()
    gpio.output(dir,0)
    gpio.output(step,0)
    ip = gpio.PWM(step,sf)
    ip.start(50)
    time.sleep(tf)
    gpio.cleanup()


ileri(1,1000)
geri(1,1000)
ileri(1,1000)
geri(1,1000)

