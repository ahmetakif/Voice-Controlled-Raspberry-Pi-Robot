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

sagin4 = 18
sagin3 = 17
sagin2 = 27
sagin1 = 22

solin4 = 26
solin3 = 4
solin2 = 12
solin1 = 8


gpio.setwarnings(False)

def init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(sagin1,gpio.OUT) 
    gpio.setup(sagin2,gpio.OUT) 
    gpio.setup(sagin3,gpio.OUT) 
    gpio.setup(sagin4,gpio.OUT)
    gpio.setup(solin1,gpio.OUT)
    gpio.setup(solin2,gpio.OUT)
    gpio.setup(solin3,gpio.OUT)
    gpio.setup(solin4,gpio.OUT) 
    gpio.setup(21,gpio.OUT)
    gpio.setup(23,gpio.IN)
    gpio.setup(24,gpio.IN)
    gpio.output(sagin1,0)
    gpio.output(sagin2,0)
    gpio.output(sagin3,0)
    gpio.output(sagin4,0)
    gpio.output(solin1,0)
    gpio.output(solin2,0)
    gpio.output(solin3,0)
    gpio.output(solin4,0)
    gpio.output(21,0)

def adim1(tf,y):
    init()
    if (y == 0): # ileri
        gpio.output(sagin1,1)
        gpio.output(sagin2,0)
        gpio.output(sagin3,0)
        gpio.output(sagin4,0)
        gpio.output(solin4,1)
        gpio.output(solin3,0)
        gpio.output(solin2,0)
        gpio.output(solin1,0)
    if (y == 1): # geri
        gpio.output(sagin1,0)
        gpio.output(sagin2,0)
        gpio.output(sagin3,0)
        gpio.output(sagin4,1)
        gpio.output(solin4,0)
        gpio.output(solin3,0)
        gpio.output(solin2,0)
        gpio.output(solin1,1)
    if (y == 2): # sol
        gpio.output(sagin1,1)
        gpio.output(sagin2,0)
        gpio.output(sagin3,0)
        gpio.output(sagin4,0)
        gpio.output(solin4,0)
        gpio.output(solin3,0)
        gpio.output(solin2,0)
        gpio.output(solin1,1)
    if (y == 3): # sag
        gpio.output(sagin1,0)
        gpio.output(sagin2,0)
        gpio.output(sagin3,0)
        gpio.output(sagin4,1)
        gpio.output(solin4,1)
        gpio.output(solin3,0)
        gpio.output(solin2,0)
        gpio.output(solin1,0)
    time.sleep(tf)
    gpio.cleanup()     
                            
def adim2(tf,y):
    init()
    if (y == 0): # ileri
        gpio.output(sagin1,0)
        gpio.output(sagin2,1)
        gpio.output(sagin3,0)
        gpio.output(sagin4,0)
        gpio.output(solin4,0)
        gpio.output(solin3,1)
        gpio.output(solin2,0)
        gpio.output(solin1,0)
    if (y == 1): # geri
        gpio.output(sagin1,0)
        gpio.output(sagin2,0)
        gpio.output(sagin3,1)
        gpio.output(sagin4,0)
        gpio.output(solin4,0)
        gpio.output(solin3,0)
        gpio.output(solin2,1)
        gpio.output(solin1,0)
    if (y == 2): # sol
        gpio.output(sagin1,0)
        gpio.output(sagin2,1)
        gpio.output(sagin3,0)
        gpio.output(sagin4,0)
        gpio.output(solin4,0)
        gpio.output(solin3,0)
        gpio.output(solin2,1)
        gpio.output(solin1,0)
    if (y == 3): # sag
        gpio.output(sagin1,0)
        gpio.output(sagin2,0)
        gpio.output(sagin3,1)
        gpio.output(sagin4,0)
        gpio.output(solin4,0)
        gpio.output(solin3,1)
        gpio.output(solin2,0)
        gpio.output(solin1,0)
    time.sleep(tf)
    gpio.cleanup()

def adim3(tf,y):
    init()
    if (y == 0): # ileri
        gpio.output(sagin1,0)
        gpio.output(sagin2,0)
        gpio.output(sagin3,1)
        gpio.output(sagin4,0)
        gpio.output(solin4,0)
        gpio.output(solin3,0)
        gpio.output(solin2,1)
        gpio.output(solin1,0)
    if (y == 1): # geri
        gpio.output(sagin1,0)
        gpio.output(sagin2,1)
        gpio.output(sagin3,0)
        gpio.output(sagin4,0)
        gpio.output(solin4,0)
        gpio.output(solin3,1)
        gpio.output(solin2,0)
        gpio.output(solin1,0)
    if (y == 2): # sol
        gpio.output(sagin1,0)
        gpio.output(sagin2,0)
        gpio.output(sagin3,1)
        gpio.output(sagin4,0)
        gpio.output(solin4,0)
        gpio.output(solin3,1)
        gpio.output(solin2,0)
        gpio.output(solin1,0)
    if (y == 3): # sag
        gpio.output(sagin1,0)
        gpio.output(sagin2,1)
        gpio.output(sagin3,0)
        gpio.output(sagin4,0)
        gpio.output(solin4,0)
        gpio.output(solin3,0)
        gpio.output(solin2,1)
        gpio.output(solin1,0)
    time.sleep(tf)
    gpio.cleanup()

def adim4(tf,y):
    init()
    if (y == 0): # ileri
        gpio.output(sagin1,0)
        gpio.output(sagin2,0)
        gpio.output(sagin3,0)
        gpio.output(sagin4,1)
        gpio.output(solin4,0)
        gpio.output(solin3,0)
        gpio.output(solin2,0)
        gpio.output(solin1,1)
    if (y == 1): # geri
        gpio.output(sagin1,1)
        gpio.output(sagin2,0)
        gpio.output(sagin3,0)
        gpio.output(sagin4,0)
        gpio.output(solin4,1)
        gpio.output(solin3,0)
        gpio.output(solin2,0)
        gpio.output(solin1,0)
    if (y == 2): # sol
        gpio.output(sagin1,0)
        gpio.output(sagin2,0)
        gpio.output(sagin3,0)
        gpio.output(sagin4,1)
        gpio.output(solin4,1)
        gpio.output(solin3,0)
        gpio.output(solin2,0)
        gpio.output(solin1,0)
    if (y == 3): # sag
        gpio.output(sagin1,1)
        gpio.output(sagin2,0)
        gpio.output(sagin3,0)
        gpio.output(sagin4,0)
        gpio.output(solin4,0)
        gpio.output(solin3,0)
        gpio.output(solin2,0)
        gpio.output(solin1,1)
    time.sleep(tf)
    gpio.cleanup()

def ileri(tf,ff):
    ff = float(ff)
    ff = ff / 1000
    for i in range(0,tf):
        adim1(ff,0)
        adim2(ff,0)
        adim3(ff,0)
        adim4(ff,0)

def geri(tf,ff):
    ff = float(ff)
    ff = ff / 1000
    for i in range(0,tf):
        adim1(ff,1)
        adim2(ff,1)
        adim3(ff,1)
        adim4(ff,1)

def sol(tf,ff):
    ff = float(ff)
    ff = ff / 1000
    for i in range(0,tf):
        adim1(ff,2)
        adim2(ff,2)
        adim3(ff,2)
        adim4(ff,2)

def sag(tf,ff):
    ff = float(ff)
    ff = ff / 1000
    for i in range(0,tf):
        adim1(ff,3)
        adim2(ff,3)
        adim3(ff,3)
        adim4(ff,3)

def dur():
    init()
    gpio.output(22,0)
    gpio.output(17,0)
    gpio.output(18,0)
    gpio.output(27,0)
    gpio.output(26,0)
    gpio.output(4,0)
    gpio.output(12,0)
    gpio.output(8,0)
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
            ileri(30,2.2)
        elif (gpio.input(23) == 1 and gpio.input(24) == 0):
            sol(30,2.2)
        elif (gpio.input(22) == 0 and gpio.input(24) == 1):
            sag(30,2.2)
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
	    y = input("hiz: ")
            print ("ileri")
            ileri(300,y)
        elif (y == "s"):
   	    y = input("hiz: ")
            print ("geri")
            geri(300,y)
        elif (y == "d"):
	    y = input("hiz: ")
            print ("sag")
            sag(300,y)
        elif (y == "a"):
	    y = input("hiz: ")
            print ("sol")
            sol(300,y)
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
