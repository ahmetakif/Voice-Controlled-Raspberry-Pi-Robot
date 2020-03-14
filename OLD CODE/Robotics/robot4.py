from SimpleCV import *
import time

cam = Camera()

img = cam.getImage()

corners = img.findCorners()

corners.show()

time.sleep(15)
