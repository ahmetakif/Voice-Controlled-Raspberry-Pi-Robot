
import SimpleCV

#display = SimpleCV.Display() #create the display to show the image
cam = SimpleCV.Camera() # initalize the camera
#normaldisplay = True # mode toggle for segment detection and display

dairedurum = 0
karedurum = 0
ucgendurum = 0

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
            img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),SimpleCV.Color.GREEN,3) # draw the circle on the main image
            dairedurum = 1
        else:
            dairedurum = 0

#    if normaldisplay: # if normal display mode
#        img.show()
#    else: # segmented mode
#        segmented.show()

    print 'daire: ', dairedurum
    return dairedurum

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
#            img.drawSquare((kareler[-1].x, kareler[-1].y), kareler[-1].radius(),SimpleCV.Color.GREEN,3) # draw the circle on the main image
            karedurum = 1
        else:
            karedurum = 0

#    if normaldisplay: # if normal display mode
#        img.show()
#    else: # segmented mode
#     
