import RPi.GPIO as gpio
import time
from mesafe import distance
import random
from sekil import dairedurum
from sekil import karedurum
from sekil import dairex
from sekil import dairey
from sekil import karex
from sekil import karey
from goruntu2 import hareket
from leds import l12345
from leds import l678910
from leds import kapa
from leds import ilerikayan
from leds import gerikayan
from leds import solakayan
from leds import sagakayan


kadrajx = 680
kadrajy = 420
kax = kadrajx / 2
kay = kadrajy / 2

aci2 = aci3 = aci4 = 6
aci = 5.5

motorhizi = 14

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(27,gpio.OUT)
    gpio.setup(17,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(23,gpio.IN)
    gpio.setup(24,gpio.IN) 
    gpio.setup(21,gpio.OUT)
    gpio.output(21,0)

def geri(tf):
    init()
    gpio.output(22,1)
    gpio.output(18,1)
    gpio.output(17,0)
    gpio.output(27,0)
    tf = float(tf)
    tf = tf / 5 / motorhizi
    gerikayan(tf)
    gpio.cleanup()

def ileri(tf):
    init()
    gpio.output(17,1)
    gpio.output(27,1)
    gpio.output(18,0)
    gpio.output(22,0)
    tf = float(tf)
    tf = tf / 5 / motorhizi
    ilerikayan(tf)
    gpio.cleanup()

def sol(tf):
    init()
    gpio.output(18,1)
    gpio.output(27,1)
    gpio.output(17,0)
    gpio.output(22,0)
    tf = float(tf)
    tf = tf / 10 / motorhizi
    solakayan(tf)
    gpio.cleanup()

def sag(tf):
    init()
    gpio.output(22,1)
    gpio.output(17,1)
    gpio.output(18,0)
    gpio.output(27,0)
    tf = float(tf)
    tf = tf / 10 / motorhizi
    sagakayan(tf)
    gpio.cleanup()

def dur():
    init()
    gpio.output(22,0)
    gpio.output(17,0)
    gpio.output(18,0)
    gpio.output(27,0)
    gpio.cleanup()

def uyari(tf):
    init()
    gpio.output(21,1)
    time.sleep(tf)
    gpio.output(21,0)
    gpio.cleanup()    

def ses(tf,ff):
    init()
    sp = gpio.PWM(21,ff)
    sp.start(70)
    time.sleep(tf)
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
    p4 = gpio.PWM(16,50)
    p4.start(6)
    p4.ChangeDutyCycle(tf)
    time.sleep(0.7)
    gpio.cleanup()

print ("          ")
print ("          ")
print ("Bu program evlere duzen getiren raspberry pi 3 robot yaziliminin 6. versiyonudur.")
print ("          ")
print ("----------v6.1----------")
print ("          ")
print ("          ")
time.sleep(2) 
print ("_____Hosgeldiniz_____")
print ("          ")
time.sleep(1)
print ("-----Komut karakterlerinin anlamlari------")
print ("          ")
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
print ("e: serbest dolasma modu")
print ("g: nesne -beyaz kup- getirme modu")
print ("q: nesne -beyaz kup veya kure- takip modu")
print ("b: fren yap(dur)")
print ("c: programdan cikis")
print ("t: hayir ifadesi")
print ("y: evet ifadesi")
print ("v: uzgun ifade")
print ("          ")
print ("          ")
time.sleep(0.5)
print ("-----Bazi bilgiler-----")
print ("          ")
print 'Motor Hizi =',motorhizi
print 'Kamera Cozunurluk:',kadrajx,'x',kadrajy
print 'Kafa yatay servo orta aci:',aci
print 'Kafa dikey servo orta aci:',aci2
print 'Kanca dikey servo orta aci:',aci3
print 'Kanca tutacak servo orta aci:',aci4
print ("          ")
   
time.sleep(2)

def kontrol():
    servo2(6)
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
                geri(2.5)
                kontrol()
            else:
                servo(5.5)
                geri(0.5)
                sol(1.1)
        else:
            servo(5.5)
            geri(0.5)
            sag(1.1)
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
                geri(2.5)
                kontrol()
            else:
                servo(5.5)
                geri(0.5)
                sag(1.1)
        else:
            servo(5.5)
            geri(0.5)
            sol(1.1)

def tersdon():
    init()
    servo2(6)
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
                geri(1.5)
                tersdon()
            else:
                servo(5.5)
                sol(1)
		while True:
		    init()
		    if (gpio.input(24) == 0):
		        sol(0.1)
		    else:
			break
        else:
            servo(5.5)
            sag(1)
	    while True:
		init()
		if (gpio.input(23) == 0):
		    sag(0.1)
		else:
		    break

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
		geri(1.5)
                tersdon()
            else:
                servo(5.5)
                sag(1)
		while True:
		    init()
		    if (gpio.input(23) == 0):
		        sag(0.1)
		    else:
			break

        else:
            servo(5.5)
            sol(1)
	    while True:
		init()
	        if (gpio.input(24) == 0):
		    sol(0.1)
		else:
		    break

def kontrol2():
    x = random.randrange(1,3)
    if (x == 1):
        print "sagabak"
        servo(3)
	kt(2)
        time.sleep(0.05)
        dis = distance('cm')
        print dis
        if dis < 15:
            print "solabak"
            servo(9)
	    kt(3)
            dis = distance('cm')
            if dis < 15:
                print "cik"
                servo(5.5)
		kt(1)
                geri(2.5)
                kontrol()
            else:
                servo(5.5)
		kt(1)
                geri(0.5)
                sol(1.1)
        else:
            servo(5.5)
	    kt(1)
            geri(0.5)
            sag(1.1)
    if (x == 2):
        print "solabak"
        servo(9)
	kt(3)
        time.sleep(0.05)
        dis = distance('cm')
        print dis
        if dis < 15:
            print"sagabak"
            servo(3)
	    kt(2)
            dis = distance('cm')
            if dis < 15:
                print "cik"
                servo(5.5)
		kt(1)
                geri(2.5)
                kontrol()
            else:
                servo(5.5)
		kt(1)
                geri(0.5)
                sag(1.1)
        else:
            servo(5.5)
	    kt(1)
            geri(0.5)
            sol(1.1)

def otomatikmod(sf):
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
	    dur()
	    if (sf == 1):
		print "kare icin bakiliyor"
		karealma()
	    elif (sf == 2):
		print "cisim birakiliyor"
		servo4(7)
		print "getirildi, gorev tamam"
		uyari(1.5)
		tersdon()
		otomatikmod(1)
	    else:
	        pass
	if dis < 15:
            print "cok dar",dis
	    if sf == 0:
                geri(0.5)
                servo(5.5)
                kontrol()
	    else:
		while True:
		    dis = distance('cm')
		    if dis < 20:
			print "yon degistirilemez"
			print "engelin kalkmasi icin bekleniyor"
			time.sleep(0.5)
		    else:
			print "engel kalkti, devam"
			break
	elif dis < 25:
            print "dar",dis
        else:
            print "temiz",dis

def karealma():
    servo2(7)
    kare = karedurum()
    print "karedurum:",kare
    time.sleep(0.5)
    if kare == 1:
        print "kare aliniyor"
	uyari(0.3)
	time.sleep(0.3)
	uyari(0.3)
	servo3(5.5)
	servo4(7)
	ileri(1.5)
	servo4(5.3)
	servo3(6.5)
	servo2(6)
	geri(1.2)
	tersdon()
	getir()
    elif kare == 0:
	print "kare yok"
	uyari(0.3)
	servo2(6)
        tersdon()
    else:
	print "hata!!!"

def getir():
    print "cisim getiriliyor"
    otomatikmod(2)	

def dt(): #dairetakip
    servo(5.5)
    servo2(6)
    aci2 = aci3 = 6
    aci = 5.5
    while True:
	dx = dairex()
	dy = dairey()
	if dx == 0 and dy == 0:
	    print 'daire yok'
	elif dy == 0:
	    print dx
	    print dy
            if dx == kax:
		servo(5.5)	   
	    elif dx > kax:
		aci = aci + 0.5
		servo(aci)
	    else:
		aci = aci - 0.5
		servo(aci)
	    if aci < 2:
		aci = 2
	    elif aci > 11:
		aci = 11
	    else:
		aci = aci
	elif dx == 0:
	    print dx
	    print dy
	    if dy == kay:
		servo(6)
	    elif dy > kay:
		aci2 = aci2 - 0.5
		servo2(aci2)
	    else:
		aci2 = aci2 + 0.5
		servo2(aci2)
	    if aci2 < 4:
		aci2 = 4
	    elif aci2 > 6.5:
		aci2 = 6.5
	    else:
	        aci2 = aci2
        else:
            print dx
            print dy
            if dx == kax:
                servo(5.5)
            elif dx > kax:
                aci = aci + 0.5
                servo(aci)
            else:
                aci = aci - 0.5
                servo(aci)
            if aci < 2:
                aci = 2
            elif aci > 11:
                aci = 11
            else:
                aci = aci
            if dy == kay:
                servo(6)
            elif dy > kay:
                aci2 = aci2 - 0.5
                servo2(aci2)
            else:
                aci2 = aci2 + 0.5
                servo2(aci2)
            if aci2 < 4:
                aci2 = 4
            elif aci2 > 6.5:
                aci2 = 6.5
            else:
                aci2 = aci2


def kt(df): #karetakip
    while True:
	ddf = df
	print "ddf:",ddf
	kare = karedurum()
	time.sleep(0.5)
	if kare == 1:
	    servo(6)
	    if ddf == 1:
	        ileri(2)
	    elif ddf == 2:
		servo(5.5)
		sag(0.7)
		ileri(2)
	    elif ddf == 3:
		servo(5.5)
		sol(0.7)
		ileri(2)
	    else:
		print "hata!!!"
		break
	else:
	    kontrol2()	    	

servo(5.5)
servo2(6)
servo3(6)
servo4(6)

dis = distance('cm')
print 'mesafe',dis

while (True):
    dis = distance('cm')
    y = raw_input("yon:")
    time.sleep(0.003)
    if(y == "w"):
        print "ileri"
        ileri(0.7)
    elif(y == "s"):
        print "geri"
        geri(0.7)
    elif(y == "a"):
        print "sol"
        sol(0.7)
    elif(y == "d"):
        print "sag"
        sag(0.7)
    elif(y == "e"):
	print "serbest dolasma moduna gecildi!...cikis icin ctrl+c"
        otomatikmod(0)
    elif(y == "g"):
	print "nesne getirme moduna gecildi!...cikis icin ctrl+c"
	otomatikmod(1)
    elif(y == "q"):
	print "nesne takip moduna gecildi!...cikis icin ctrl+c"
	uyari(0.7)
        while (True):
	    daire = dairedurum()
	    kare = karedurum()
	    hare = hareket()
	    time.sleep(0.1)
	    if hare == 1:
		print 'hareket algilandi'
	    else:
		print 'hareket yok'
	    if daire == 1:
	        print "daire algilandi"
		dt()
	    else:
	        print "daire yok"
 	    if kare == 1:
		print "kare algilandi"
		servo(6)
		servo2(6.5)
		kt(1)
	    else:
		print "kare yok"

    elif(y == "c"):
        print "hoscakal"
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
        print 'tutacak aciliyor,aci = ',aci
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
    elif (y == "v"):
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
#      	y = input("sesfrekansi: ")
        print ("ses cikariliyor")
        ses(1,666)	
    else:
        print ("anlamadim tekrar dene")
        dur()
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
         

