import os
import RPi.GPIO as gpio
import time
from mesafe import distance

motorhizi = 1

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

print ("          ")
print ("hareketsesli yazilimi google speech api sesli komutlari ile robotu kontol etmek için yazilmistir")
print ("          ")
print ("hosgeldiniz")
print ("          ")
time.sleep(1)

#print ("komut karakterlerinin anlamlari:")
#print ("w: ileri git")
#print ("s: geri git")
#print ("a: sola don")
#print ("d: saga don")
#print ("j: kafayi duz konuma getir")
#print ("u: kafayi yukari kaldir")
#print ("n: kafayi asagi indir")
#print ("h: kafayi sola cevir")
#print ("k: kafayi saga cevir")
#print ("r: kolu kaldir")
#print ("f: kolu indir")
#print ("z: tutacagi ac")
#print ("x: tutacagi kapat")
#print ("b: fren yap(dur)")
#print ("c: programdan cikis")
#print ("t: hayir ifadesi")
#print ("y: evet ifadesi")
#print ("g: uzgun ifade")
#print ("        ")   
#time.sleep(2)

#os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_active.wav &")



aci2 = aci3 = aci4 = 6
aci = 5.5
  
time.sleep(0.03)

def sesli(y):

        dis = distance('cm')
        print ('mesafe',dis)
      
        aci2 = aci3 = aci4 = 6
        aci = 5.5 


#        if (y == "w"):
#	    y = input("hiz(0-100): ")
#            print ("ileri")
#            ileri(0.2,100)
#        elif (y == "s"):
#	y = input("hiz(0-100): ")
#            print ("geri")
#            geri(0.2,100)
#        elif (y == "d"):
#	    y = input("hiz(0-100): ")
#            print ("sag")
#            sag(0.2,100)
#        elif (y == "a"):
#           y = input("hiz(0-100): ")
#            print ("sol")
#            sol(0.2,100)
#        elif (y == "q"):
#            cizgi()
#        elif (y == "c"):
#            print ("hoscakal")
#            break

        if (y == 0):
            print ("duz bakiliyor aci = 5.5  aci2 =6")
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_ping.wav &")
            servo(5.5)
            servo2(6)
            aci = 5.5
            aci2 = 6
        elif (y == 1):
            print ('asagi bakiliyor,aci2 = ',aci2)
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_ping.wav &")
            aci2 = 7.5
            servo2(aci2)
        elif (y == 2):
            print ('asagi bakiliyor,aci2 = ',aci2)
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_ping.wav &")
            aci2 = 4.5
            servo2(aci2)
        elif (y == 3):
            aci = 7
            print ('sola bakiliyor,aci = ',aci)
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_ping.wav &")
            servo(aci)
        elif (y == 4):
            aci = 4
            print ('saga bakiliyor,aci = ',aci)
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_ping.wav &")
            servo(aci)
        elif (y == 13):
            print ('kol sola donuyor')
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_ping.wav &")
            stepper(30,3,1)
        elif (y == 14):
            print ('kol saga donuyor')
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_ping.wav &")
            stepper(30,3,0)
        elif (y == 5):
            aci3 = 8
            print ('kol yukari,aci = ',aci3)
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_ping.wav &")
            servo3(aci3)
        elif (y == 6):
            aci3 = 6
            print ('kol asagi,aci = ',aci3)
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_ping.wav &")
            servo3(aci3)
        elif (y == 7):
            aci4 = 7.5
            print ('tutacak aciliyor,aci = ',aci4)
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_ping.wav &")
            servo4(aci4)
        elif (y == 8):
            aci4 = 4.5
            print ('tutacak kapatiliyor,aci = ',aci4)
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_ping.wav &")
            servo4(aci4)
        elif (y == 9):
            print ("fren yapiliyor")
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_retract.wav &")
            dur()
        elif (y == 10):
            print ("evet ifade ediliyor")
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_turretshotbylaser02.wav &")
            servo2(6)
            servo2(5)
            servo2(6)
        elif (y == 11):
            print ("hayir ifade ediliyor")
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_turretlaunched04.wav &")
            servo(5.5)
            servo(4.5)
            servo(6.5)
            servo(5.5)
        elif (y == 12):
            print ("  :(  ")
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_turretwitnessdeath11.wav &")
            servo2(6.6)
            servo(5.5)
            servo(6.5)
            servo(4.5)
            servo(6.5)
            servo(4.5)
            servo(6.5)
            servo2(6)
            servo(5.5)
#        elif (y == "o"):
#      	    y = input("sesfrekansi: ")
#            print ("ses cikariliyor")
#            ses(1,666)	
        else:
            print ("anlamadim tekrar dene")
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_alert.wav &")
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_sp_sabotage_factory_good_fail03.wav &")
            os.system("aplay -vv /home/pi/Robotics/PortalTurret/Turret_turret_tipped_4.wav &")
            dur()
            pass
        
