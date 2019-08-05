import RPi.GPIO as gpio
import time
from mesafe import distance

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(27,gpio.OUT)
    gpio.setup(12,gpio.OUT)
    gpio.setup(25,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    
def ileri(tf):
    init()
    gpio.output(27,1)
    gpio.output(22,1)
    gpio.output(12,0)
    gpio.output(25,0)
    time.sleep(tf)
    gpio.cleanup()

def geri(tf):
    init()
    gpio.output(12,1)
    gpio.output(25,1)
    gpio.output(27,0)
    gpio.output(22,0)
    time.sleep(tf)
    gpio.cleanup()

def sol(tf):
    init()
    gpio.output(12,1)
    gpio.output(22,1)
    gpio.output(27,0)
    gpio.output(25,0)
    time.sleep(tf)
    gpio.cleanup()

def sag(tf):
    init()
    gpio.output(27,1)
    gpio.output(25,1)
    gpio.output(12,0)
    gpio.output(22,0)
    time.sleep(tf)
    gpio.cleanup()

while (True):
    dis = distance('cm')
    print dis
    y = raw_input("y:")
    time.sleep(0.003)
    if(y == "w"):
        print "ileri"
        ileri(0.4)
    elif(y == "s"):
        print "geri"
        geri(0.4)
    elif(y == "a"):
        print "sol"
        sol(0.4)
    elif(y == "d"):
        print "sag"
        sag(0.4)
    else:
        print "tkrr"
        pass
    if dis < 15:
        print "cok dar",dis 
        geri(0.8)
        sag(0.5)
    elif dis < 25:
        print "dar",dis
        geri(0.6)
        sol(0.4)
    else:
         print "temiz"
#        ileri(0.4)

