import RPi.GPIO as gpio 
import time 

while (True):
    def servo(tf):
        gpio.setmode(gpio.BCM)
        gpio.setup(16,gpio.OUT)
        p = gpio.PWM(16,50)
        p.start(7.5)
        p.ChangeDutyCycle(tf)
        time.sleep(1)
        gpio.cleanup()

    a = input("aci:")
    servo(a)
             
