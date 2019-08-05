import os
import RPi.GPIO as gpio
import time
import random
from mesafe import distance

motorhizi = 2.5
hiz = 100

aci2 = aci3 = aci4 = 6
aci = 5.5

in4 = 26
in3 = 4
in2 = 12
in1 = 8

solled = 9
sagled = 11

gpio.setwarnings(False)

def init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(22,gpio.OUT)
    gpio.setup(27,gpio.OUT)
    gpio.setup(17,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(in4,gpio.OUT)
    gpio.setup(in3,gpio.OUT)
    gpio.setup(in2,gpio.OUT)
    gpio.setup(in1,gpio.OUT)
    gpio.setup(21,gpio.OUT)
    gpio.setup(solled,gpio.OUT)
    gpio.setup(sagled,gpio.OUT)
    gpio.setup(23,gpio.IN)
    gpio.setup(24,gpio.IN)    
    gpio.output(22,0)
    gpio.output(18,0)
    gpio.output(17,0)
    gpio.output(27,0)
    gpio.output(in4,0)
    gpio.output(in3,0)
    gpio.output(in2,0)
    gpio.output(in1,0)
    gpio.output(21,0)
    gpio.output(solled,0)
    gpio.output(sagled,0)

def ileri(tf,ff):
    init()
    gpio.output(17,0)
    gpio.output(22,0)
    ip = gpio.PWM(27,50)
    ip2 = gpio.PWM(18,50)
    ip.start(ff)
    ip2.start(ff)
    tf = float(tf)
    tf = tf / motorhizi
    time.sleep(tf)
    gpio.cleanup()

def geri(tf,ff):
    init()
    gpio.output(18,0)
    gpio.output(27,0)
    gp = gpio.PWM(22,50)
    gp2 = gpio.PWM(17,50)
    gp.start(ff)
    gp2.start(ff)
    tf = float(tf)
    tf = tf / motorhizi
    time.sleep(tf)
    gpio.cleanup()

def sol(tf,ff):
    init()
    gpio.output(17,0)
    gpio.output(27,0)
    sp = gpio.PWM(22,50)
    sp2 = gpio.PWM(18,50)
    sp.start(ff)
    sp2.start(ff)
    tf = float(tf)
    tf = tf / motorhizi
    time.sleep(tf)
    gpio.cleanup()

def sag(tf,ff):
    init()
    gpio.output(18,0)
    gpio.output(22,0)
    sap = gpio.PWM(27,50)
    sap2 = gpio.PWM(17,50)
    sap.start(ff)
    sap2.start(ff)
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

def adim1(tf,y):
    init()
    if (y == 1): # sol
        gpio.output(in1,1)
        gpio.output(in2,0)
        gpio.output(in3,0)
        gpio.output(in4,0)
    if (y == 0): # sag
        gpio.output(in1,0)
        gpio.output(in2,0)
        gpio.output(in3,0)
        gpio.output(in4,1)
    time.sleep(tf)
    gpio.cleanup()

def adim2(tf,y):
    init()
    if (y == 1): # sol
        gpio.output(in1,0)
        gpio.output(in2,1)
        gpio.output(in3,0)
        gpio.output(in4,0)
    if (y == 0): # sag
        gpio.output(in1,0)
        gpio.output(in2,0)
        gpio.output(in3,1)
        gpio.output(in4,0)
    time.sleep(tf)
    gpio.cleanup()

def adim3(tf,y):
    init()
    if (y == 1): # sol
        gpio.output(in1,0)
        gpio.output(in2,0)
        gpio.output(in3,1)
        gpio.output(in4,0)
    if (y == 0): # sag
        gpio.output(in1,0)
        gpio.output(in2,1)
        gpio.output(in3,0)
        gpio.output(in4,0)
    time.sleep(tf)
    gpio.cleanup()

def adim4(tf,y):
    init()
    if (y == 1): # sol
        gpio.output(in1,0)
        gpio.output(in2,0)
        gpio.output(in3,0)
        gpio.output(in4,1)
    if (y == 0): # sag
        gpio.output(in1,1)
        gpio.output(in2,0)
        gpio.output(in3,0)
        gpio.output(in4,0)
    time.sleep(tf)
    gpio.cleanup()

def stepper(tf,ff,yf):
    ff = float(ff)
    ff = ff / 1000
    if (yf == 0): # sag
        for i in range(0,tf):
            adim1(ff,0)
            adim2(ff,0)
            adim3(ff,0)
            adim4(ff,0)
    if (yf == 1): # sol
        for i in range(0,tf):
            adim1(ff,1)
            adim2(ff,1)
            adim3(ff,1)
            adim4(ff,1)

def servo(tf):
    gpio.setmode(gpio.BCM)
    gpio.setup(5,gpio.OUT)
    p = gpio.PWM(5,50)
    p.start(5.5)
    p.ChangeDutyCycle(tf)
    time.sleep(0.7)
    gpio.cleanup()    

def servo2(tf):
    gpio.setmode(gpio.BCM)
    gpio.setup(6,gpio.OUT)
    p2 = gpio.PWM(6,50)
    p2.start(6)
    p2.ChangeDutyCycle(tf)
    time.sleep(0.7)
    gpio.cleanup()

def servo3(tf):
    gpio.setmode(gpio.BCM)
    gpio.setup(20,gpio.OUT)
    p3 = gpio.PWM(20,50)
    p3.start(6)
    p3.ChangeDutyCycle(tf)
    time.sleep(0.7)
    gpio.cleanup()

def servo4(tf):
    gpio.setmode(gpio.BCM)
    gpio.setup(16,gpio.OUT)
    p3 = gpio.PWM(16,50)
    p3.start(6)
    p3.ChangeDutyCycle(tf)
    time.sleep(0.7)
    gpio.cleanup()

def ses(tf,ff):
    init()
    sp = gpio.PWM(21,ff)
    sp.start(70)
    time.sleep(tf)
    gpio.cleanup()

def led(ff,tf,sf):
    init()
    sp = gpio.PWM(solled,500)
    sap = gpio.PWM(sagled,500)
    if (sf == 0):
        sp.start(ff)
        time.sleep(tf)
        gpio.cleanup()
    elif (sf == 1):
        sap.start(ff)
        time.sleep(tf)
        gpio.cleanup()
    elif (sf == 2):
        sp.start(ff)
        sap.start(ff)
        time.sleep(tf)
        gpio.cleanup()

def kontrol():
    x = random.randrange(1,3)
    if (x == 1):
        print ("sagabak")
        servo(3)
        time.sleep(0.05)
        dis = distance('cm')
        print (dis)
        if dis < 15:
            print ("solabak")
            servo(9)
            dis = distance('cm')
            if dis < 15:
                print ("cik")
                servo(5.5)
                geri(2,hiz)
            else:
                servo(5.5)
                geri(0.5,hiz)
                sol(0.7,hiz)
        else:
            servo(5.5)
            geri(0.5,hiz)
            sag(0.7,hiz)
    if (x == 2):
        print ("solabak")
        servo(9)
        time.sleep(0.05)
        dis = distance('cm')
        print (dis)
        if dis < 15:
            print ("sagabak")
            servo(3)
            dis = distance('cm')
            if dis < 15:
                print ("cik")
                servo(5.5)
                geri(2,hiz)
            else:
                servo(5.5)
                geri(0.5,hiz)
                sag(0.7,hiz)
        else:
            servo(5.5)
            geri(0.5,hiz)
            sol(0.7,hiz)


print ("          ")
print ("otonomgorev yazilimi google speech api sesli komutlari ile robotun otonom hareket etmesi icin yazilmistir")
print ("          ")
time.sleep(1)

def cizgi():
    os.system("sudo pkill -9 -f main.py")
    while (True):
        dis = distance('cm')
        init()
        if (gpio.input(23) == 0 and gpio.input(24) == 0):
            ileri(0.1,hiz)
        elif (gpio.input(23) == 1 and gpio.input(24) == 0):
            sol(0.1,hiz)
        elif (gpio.input(23) == 0 and gpio.input(24) == 1):
            sag(0.1,hiz)
        else:
            pass
        if dis < 15:
            print ("cok dar",dis)
            geri(0.5,hiz)
            servo(5.5)
            kontrol()
        elif dis < 25:
            print ("dar",dis)
        else:
            print ("temiz",dis)
        dur()



aci2 = aci3 = aci4 = 6
aci = 5.5

cizgi()
