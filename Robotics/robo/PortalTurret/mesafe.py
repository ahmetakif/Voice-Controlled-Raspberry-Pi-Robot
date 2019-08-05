import RPi.GPIO as gpio
import time

def distance(measure='cm'):
    gpio.setmode(gpio.BCM)
    trig = 13
    echo = 19
    gpio.setup(trig,gpio.OUT)
    gpio.output(trig,0)
    gpio.setup(echo,gpio.IN)
    
    time.sleep(0.01)

    gpio.output(trig,1)
    time.sleep(0.00001)
    gpio.output(trig,0)

    while gpio.input(echo) == 0:
            pass
    start = time.time()

    while gpio.input(echo) == 1:
            pass
    stop = time.time()

    distance = (stop - start) * 17000

    gpio.cleanup()
    return distance

#print (distance('cm'))


