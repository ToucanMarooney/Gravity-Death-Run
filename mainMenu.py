import pyglet, random
from pyglet.gl import *

windowWidth = 640
windowHeight = 480
gameWindow = pyglet.window.Window(windowWidth, windowHeight)
FPS = 60
squareSize = 32


#Squares to be drawn on-screen in the background. 
class Square:
    def __init__(self, x, y, height, width, columnColour):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        #colour. Originally set to universal colour (for the column the square belongs to)
        self.colour = columnColour
        #Shade. random number to start with, gradually increases to 255 then after a pause returns to 0 and gradually increases again
        self.shade = 1

    def drawSelf(self):
        pyglet.graphics.draw(4, GL_QUADS, ('v2i', (
        self.x, self.y + self.height, self.x + self.width, self.y + self.height, self.x + self.width, self.y, self.x,
        self.y)), ('c3B', (self.colour[0], self.colour[1], self.colour[2],
                           self.colour[0], self.colour[1], self.colour[2],
                           self.colour[0], self.colour[1], self.colour[2],
                           self.colour[0], self.colour[1], self.colour[2],)))


#Create the squares and set them to a grid constrained to the screen size.
squares = []
for i in range(windowWidth/squareSize):
    for ii in range(windowHeight/squareSize):
		squares.append(Square(i*squareSize, ii*squareSize, squareSize, squareSize, (56, 57, 58)))
		
#This method of setting colours for columns may be deemed inefficient and may not be used.
#Choose the colours from a list of colours. 

lblue = (51,255,255)
blue = (0,0,255)
dblue = (0,0,102)
red = (255,0,0)
pink = (255,51,153)
purple = (153,51,255)
lgreen = (204,255,0)
green = (51,255,0)
dgreen = (0,102,0)
yellow = (255,255,255)
orange = (153,255,51)

colours = []
colours.append(lblue)
colours.append(blue)
colours.append(dblue)
colours.append(red)
colours.append(pink)
colours.append(purple)
colours.append(green)
colours.append(dgreen)
colours.append(lgreen)
colours.append(yellow)
colours.append(orange)

possibleColours = []
for i in range(windowWidth/squareSize):
	possibleColours.append(colours[random.randint(0,10)])
	print i

for i in range(windowWidth/squareSize):
	for ii in squares:
		if i*squareSize == ii.x:
			ii.colour = possibleColours[i]
			
	




@gameWindow.event
def on_draw():
    gameWindow.clear()
    for square in squares:
        square.drawSelf()


def update(dt):
    pass


pyglet.clock.schedule_interval(update, 1.0 / 120.0)
pyglet.app.run()