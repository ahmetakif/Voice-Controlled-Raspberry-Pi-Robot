import RPi.GPIO as gpio
import time
from mesafe import distance
from leds import kapa
from leds import sagakayan
from leds import solakayan
from leds import ilerikayan
from leds import gerikayan
from leds import l12345
from leds import l678910

aci2 = aci3 = aci4 = 6
aci = 5.5

sagdir = 18
sagstep = 17
solstep = 27
soldir = 22

gpio.setwarnings(False)

def init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(solstep,gpio.OUT) 
    gpio.setup(sagstep,gpio.OUT) 
    gpio.setup(sagdir,gpio.OUT) 
    gpio.setup(soldir,gpio.OUT) 
    gpio.setup(21,gpio.OUT)
    gpio.setup(23,gpio.IN)
    gpio.setup(24,gpio.IN)
    gpio.output(solstep,0)
    gpio.output(sagstep,0)
    gpio.output(sagdir,0)
    gpio.output(soldir,0)
    gpio.output(21,0)

def ileri(tf,ff):
    init()
    ip = gpio.PWM(sagstep,ff)
    ip2 = gpio.PWM(solstep,ff)
    ip.start(50)
    ip2.start(50)
    gpio.output(soldir,1)
    gpio.output(sagdir,1)
    tf = float(tf)
    tf = tf / 5
    ilerikayan(tf) 
    gpio.cleanup()

def geri(tf,ff):
    init()
    ip = gpio.PWM(sagstep,ff)
    ip2 = gpio.PWM(solstep,ff)
    ip.start(50)
    ip2.start(50)
    gpio.output(soldir,0)
    gpio.output(sagdir,0)
    tf = float(tf)
    tf = tf / 5
    gerikayan(tf)
    gpio.cleanup()

def sol(tf,ff):
    init()
    ip = gpio.PWM(sagstep,ff)
    ip2 = gpio.PWM(solstep,ff)
    ip.start(50)
    ip2.start(50)
    gpio.output(soldir,0)
    gpio.output(sagdir,1)
    tf = float(tf)
    tf = tf / 5
    solakayan(tf)
    gpio.cleanup()

def sag(tf,ff):
    init()
    ip = gpio.PWM(sagstep,ff)
    ip2 = gpio.PWM(solstep,ff)
    ip.start(50)
    ip2.start(50)
    gpio.output(soldir,1)
    gpio.output(sagdir,0)
    tf = float(tf)
    tf = tf / 5
    sagakayan(tf)
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

print ("hosgeldiniz")
print ("          ")
time.sleep(1)
print ("komut karakterlerinin anlamlari:")
print ("w: ileri git")
print ("s: geri git")
print ("a: sola don")
print ("d: saga don")
print ("j: kafayi duz konuma getir")
print ("u: kafayi yukari kaldir")
print ("n: kafayi asagi indir")
print ("h: kafayi sola cevir")
print ("k: kafayi saga cevir")
print ("r: kolu kaldir")
print ("f: kolu indir")
print ("z: tutacagi ac")
print ("x: tutacagi kapat")
print ("b: fren yap(dur)")
print ("c: programdan cikis")
print ("t: hayir ifadesi")
print ("y: evet ifadesi")
print ("g: uzgun ifade")
print ("        ")   
time.sleep(2)

def cizgi(): #sure kisitlamali
    int = 0
    for int in range(1,200):
        init()
        if (gpio.input(23) == 0 and gpio.input(24) == 0):
            ileri(0.1,100)
        elif (gpio.input(23) == 1 and gpio.input(24) == 0):
            sol(0.1,100)
        elif (gpio.input(22) == 0 and gpio.input(24) == 1):
            sag(0.1,100)
        else:
            dur()
    dur()
    main()

def main():
    aci2 = aci3 = aci4 = 6
    aci = 5.5
    while (True):
        dis = distance('cm')
        print 'mesafe',dis
        y = raw_input("komut karakteri:")
        time.sleep(0.03)
        if (y == "w"):
#	    y = input("hiz: ")
            print ("ileri")
            ileri(2,500)
        elif (y == "s"):
#	y = input("hiz(0-100): ")
            print ("geri")
            geri(2,500)
        elif (y == "d"):
#	    y = input("hiz(0-100): ")
            print ("sag")
            sag(2,500)
        elif (y == "a"):
#	    y = input("hiz(0-100): ")
            print ("sol")
            sol(2,500)
        elif (y == "q"):
	    cizgi()
        elif (y == "c"):
            print ("hoscakal")
            break
        elif (y == "j"):
            print ("duz bakiliyor aci = 5.5  aci2 =6")
            servo(5.5)
            servo2(6)
            aci = 5.5
            aci2 = 6
        elif (y == "n"):
            aci2 = aci2 + 0.5
            print 'asagi bakiliyor,aci2 = ',aci2
            servo2(aci2)
        elif (y == "u"):
            aci2 = aci2 - 0.5
            print 'yukari bakiliyor,aci2 = ',aci2
            servo2(aci2)
        elif (y == "h"):
            aci = aci + 0.5
            print 'sola bakiliyor,aci = ',aci
            servo(aci)
        elif (y == "k"):
            aci = aci - 0.5
            print 'saga bakiliyor,aci = ',aci
            servo(aci)
        elif (y == "r"):
            aci3 = aci3 + 0.5
            print 'kanca yukari,aci = ',aci3
            servo3(aci3)
        elif (y == "f"):
            aci3 = aci3 - 0.5
            print 'kanca asagi,aci = ',aci3
            servo3(aci3)
        elif (y == "z"):
	    aci4 = aci4 + 0.5
       	    print 'tutacak aciliyor,aci = ',aci4
	    servo4(aci4)
        elif (y == "x"):
            aci4 = aci4 - 0.5
            print 'tutacak kapatiliyor,aci = ',aci4
            servo4(aci4)
        elif (y == "b"):
            print ("fren yapiliyor")
            dur()
        elif (y == "y"):
            print ("evet ifade ediliyor")
	    servo2(6)
	    servo2(5)
	    servo2(6)
        elif (y == "t"):
	    print ("hayir ifade ediliyor")
	    servo(6)
	    servo(5)
	    servo(7)
	    servo(6)
        elif (y == "g"):
	    print ("  :(  ")
	    servo2(6.6)
	    servo(5.5)
	    servo(6.5)
	    servo(5.5)
	    servo(6.5)
	    servo(5.5)
	    servo(6.5)
	    servo2(6)
	    servo(6)
        elif (y == "o"):
#      	    y = input("sesfrekansi: ")
            print ("ses cikariliyor")
            ses(1,666)	
        else:
            print ("anlamadim tekrar dene")
            dur()
            pass

main()
