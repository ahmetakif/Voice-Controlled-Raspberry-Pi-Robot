from SimpleCV import *

cam = Camera()
display = Display((480,320))

while True:
    display.checkEvents()
    img = cam.getImage()
    img = img.findCorners()
    img.show()
    if display.mouseLeft:
	img = img.edges()
	img.drawText('X-ray aktiflestirildi')
	img.show()
    elif display.mouseRight:
	facelayer = DrawingLayer((img.width, img.height))
	facebox_dim = (200,200)
	center_point = (img.width / 2, img.height / 2)
	facebox = facelayer.centeredRectangle(center_point, facebox_dim, color=Color.GREEN)
	circlelayer = DrawingLayer((img.width, img.height))
	circlelayer.circle(center_point, 40, color=Color.BLUE)
	img.addDrawingLayer(facelayer)
	img.addDrawingLayer(circlelayer)
	img.applyLayers()
	img.show()
