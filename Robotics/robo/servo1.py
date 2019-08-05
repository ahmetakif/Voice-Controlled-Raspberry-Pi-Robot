import RPi.GPIO as gpio
import time

while (True):
    def servo(tf):
        gpio.setmode(gpio.BCM)
        gpio.setup(5,gpio.OUT)
        p = gpio.PWM(5,50)
        p.start(7.5)
        p.ChangeDutyCycle(tf)
        time.sleep(1)
        gpio.cleanup()

    a = input("aci:")
    servo(a)
