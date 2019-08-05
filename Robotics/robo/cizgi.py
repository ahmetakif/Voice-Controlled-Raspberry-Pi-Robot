import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(17,gpio.OUT)
    gpio.setup(27,gpio.OUT)
    gpio.setup(23,gpio.IN)
    gpio.setup(24,gpio.IN)
    
def ileri(tf):
    init()
    gpio.output(18,1)
    gpio.output(22,1)
    gpio.output(17,0)
    gpio.output(27,0)
    time.sleep(tf)
    gpio.cleanup()

def geri(tf):
    init()
    gpio.output(17,1)
    gpio.output(27,1)
    gpio.output(18,0)
    gpio.output(22,0)
    time.sleep(tf)
    gpio.cleanup()

def sag(tf):
    init()
    gpio.output(17,1)
    gpio.output(22,1)
    gpio.output(18,0)
    gpio.output(27,0)
    time.sleep(tf)
    gpio.cleanup()

def sol(tf):
    init()
    gpio.output(18,1)
    gpio.output(27,1)
    gpio.output(17,0)
    gpio.output(22,0)
    time.sleep(tf)
    gpio.cleanup()

def dur():
    init()
    gpio.output(18,0)
    gpio.output(27,0)
    gpio.output(17,0)
    gpio.output(22,0)
    gpio.cleanup()


while (True):
    init()
    if (gpio.input(23) == 0 and gpio.input(24) == 0):
        ileri(0.07)
    elif (gpio.input(23) == 1 and gpio.input(24) == 0):
        sol(0.07)
    elif (gpio.input(23) == 0 and gpio.input(24) == 1):
        sag(0.07) 
    else:
        pass        
    dur()
