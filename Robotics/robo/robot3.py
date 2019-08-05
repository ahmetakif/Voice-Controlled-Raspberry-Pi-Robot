import RPi.GPIO as gpio
import time
from mesafe import distance
import random

motorhizi = 2.5

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(27,gpio.OUT)
    gpio.setup(17,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(23,gpio.IN)
    gpio.setup(24,gpio.IN) 

def geri(tf):
    init()
    gpio.output(22,1)
    gpio.output(17,1)
    gpio.output(18,0)
    gpio.output(27,0)
    tf = float(tf)
    tf = tf / motorhizi
    time.sleep(tf)
    gpio.cleanup()

def ileri(tf):
    init()
    gpio.output(18,1)
    gpio.output(27,1)
    gpio.output(17,0)
    gpio.output(22,0)
    tf = float(tf)
    tf = tf / motorhizi
    time.sleep(tf)
    gpio.cleanup()

def sol(tf):
    init()
    gpio.output(18,1)
    gpio.output(22,1)
    gpio.output(17,0)
    gpio.output(27,0)
    tf = float(tf)
    tf = tf / motorhizi
    time.sleep(tf)
    gpio.cleanup()

def sag(tf):
    init()
    gpio.output(27,1)
    gpio.output(17,1)
    gpio.output(18,0)
    gpio.output(22,0)
    tf = float(tf)
    tf = tf / motorhizi
    time.sleep(tf)
    gpio.cleanup()

def dur():
    init()
    gpio.output(22,0)
    gpio.output(17,0)
    gpio.output(18,0)
    gpio.output(27,0)
    gpio.cleanup()

def servo(tf):
    gpio.setmode(gpio.BCM)
    gpio.setup(5,gpio.OUT)
    p = gpio.PWM(5,50)
    p.start(5.5)
    p.ChangeDutyCycle(tf)
    time.sleep(0.7)
    gpio.cleanup()

def kontrol():
    x = random.randrange(1,3)
    if (x == 1):
        print "sagabak"
        servo(3)
        time.sleep(0.05)
        dis = distance('cm')
        print dis
        if dis < 15:
            print "solabak"
            servo(9)
            dis = distance('cm')
            if dis < 15:
                print "cik"
                servo(5.5)
                geri(2)
            else:
                servo(5.5)
                geri(0.5)
                sol(0.7)
        else:
            servo(5.5)
            geri(0.5)
            sag(0.7)
    if (x == 2):
        print "solabak"
        servo(9)
        time.sleep(0.05)
        dis = distance('cm')
        print dis
        if dis < 15:
            print"sagabak"
            servo(3)
            dis = distance('cm')
            if dis < 15:
                print "cik"
                servo(5.5)
                geri(2)
            else:
                servo(5.5)
                geri(0.5)
                sag(0.7)
        else:
            servo(5.5)
            geri(0.5)
            sol(0.7)

while (True):
    servo(5.5)
    dis = distance('cm')
    y = raw_input("yon:")
    time.sleep(0.003)
    if(y == "w"):
        print "ileri"
        ileri(0.5)
    elif(y == "s"):
        print "geri"
        geri(0.5)
    elif(y == "a"):
        print "sol"
        sol(0.5)
    elif(y == "d"):
        print "sag"
        sag(0.5)
    elif(y == "r"):
        print "Otomatik moda geciliyor!...cikis icin ctrl+c"
        while (True):
            dis = distance('cm')
            init()
            if (gpio.input(23) == 0 and gpio.input(24) == 0):
                ileri(0.1)            
            elif (gpio.input(23) == 1 and gpio.input(24) == 0):
                sol(0.1)
            elif (gpio.input(23) == 0 and gpio.input(24) == 1):
                sag(0.1)
            else:
                pass
            if dis < 15:
                print "cok dar",dis
                geri(0.5)
                servo(5.5)
                kontrol()
            elif dis < 25:
                print "dar",dis
            else:
                print "temiz",dis
            dur()
    elif(y == "c"):
        print "hoscakal"
        break
    else:
        print "tkrr"
        pass
    if dis < 15:
        print "cok dar",dis
        geri(0.2) 
        kontrol()
    elif dis < 25:
        print "dar",dis
        
    else:
        print "temiz",dis
        servo(5.5)       
         

