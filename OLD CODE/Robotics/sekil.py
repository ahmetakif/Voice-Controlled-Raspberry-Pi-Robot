import SimpleCV
import time

#display = SimpleCV.Display() #create the display to show the image
cam = SimpleCV.Camera() # initalize the camera
#normaldisplay = True # mode toggle for segment detection and display

karedurum = 0
dairedurum = 0
dairex = 0
dairey = 0
karex = 0
karey = 0

#while display.isNotDone(): # loop until we tell the program to stop
def dairedurum():

#    if display.mouseRight: # if right mouse clicked, change mode
#        normaldisplay = not(normaldisplay)
#        print "Display Mode:", "Normal" if normaldisplay else "Segmented"

    img = cam.getImage().flipHorizontal() # grab image from camera
    dist = img.colorDistance(SimpleCV.Color.BLACK).dilate(2) # try to separate colors in image
    segmented = dist.stretch(200,255) # really try to push out white colors
    blobs = segmented.findBlobs() # search the image for blob objects
    if blobs: # if blobs are found
        circles = blobs.filter([b.isCircle(0.2) for b in blobs]) # filter out only circle shaped blobs
        if circles:
	    dairedurum = 1 
#            img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),SimpleCV.Color.GREEN,3) # draw the circle on the main image
	    print 'daire: ',dairedurum
        else:
	    dairedurum = 0
	    print 'daire: ',dairedurum

#    if normaldisplay: # if normal display mode
#        img.show()
#    else: # segmented mode
#        segmented.show()

    return dairedurum

def dairex():
    img = cam.getImage().flipHorizontal()
    dist = img.colorDistance(SimpleCV.Color.BLACK).dilate(2)
    segmented = dist.stretch(200,255)
    blobs = segmented.findBlobs()
    if blobs:
        circles = blobs.filter([b.isCircle(0.2) for b in blobs])
        if circles:
            dairex = circles[-1].x
            print 'dairex: ',dairex
        else:
	    dairex = 0
    return dairex

def dairey():
    img = cam.getImage().flipHorizontal()
    dist = img.colorDistance(SimpleCV.Color.BLACK).dilate(2)
    segmented = dist.stretch(200,255)
    blobs = segmented.findBlobs()
    if blobs:
        circles = blobs.filter([b.isCircle(0.2) for b in blobs])
        if circles:
            dairey = circles[-1].y
            print 'dairey: ',dairey
        else:
	    dairey = 0
    return dairey

def karedurum():

#    if display.mouseRight: # if right mouse clicked, change mode
#        normaldisplay = not(normaldisplay)
#        print "Display Mode:", "Normal" if normaldisplay else "Segmented"

    img = cam.getImage().flipHorizontal() # grab image from camera
    dist = img.colorDistance(SimpleCV.Color.BLACK).dilate(2) # try to separate colors in image
    segmented = dist.stretch(200,255) # really try to push out white colors
    blobs = segmented.findBlobs() # search the image for blob objects
    if blobs: # if blobs are found
        kareler = blobs.filter([b.isSquare(0.2) for b in blobs]) # filter out only circle shaped blobs
        if kareler:
#            img.drawSquare((kareler[-1].x, kareler[-1].y), kareler[-1].radius(),SimpleCV.Color.GREEN,3)$
            karedurum = 1
            print 'kare: ',karedurum
        else:
            karedurum = 0
            print 'kare: ',karedurum

#    if normaldisplay: # if normal display mode
#        img.show()
#    else: # segmented mode
#        segmented.show()

    return karedurum

def karex():

    img = cam.getImage().flipHorizontal()
    dist = img.colorDistance(SimpleCV.Color.BLACK).dilate(2)
    segmented = dist.stretch(200,255)
    blobs = segmented.findBlobs()
    if blobs:
        kareler = blobs.filter([b.isSquare(0.2) for b in blobs])
        if kareler:
            karex = kareler[-1].x
            print 'karex: ',karex
        else:
            karex = 0
    return karex


def karey():

    img = cam.getImage().flipHorizontal()
    dist = img.colorDistance(SimpleCV.Color.BLACK).dilate(2)
    segmented = dist.stretch(200,255)
    blobs = segmented.findBlobs()
    if blobs:
        kareler = blobs.filter([b.isSquare(0.2) for b in blobs])
        if kareler:
            karey = kareler[-1].y
            print 'karey: ',karey
        else:
            karey = 0
    return karey
