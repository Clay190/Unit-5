#Clay Kynor
#11/20/17
#snow.py - making snow fall from the sky 

from ggame import *
from random import randint

WIDTH = 100
HEIGHT = 100
SNOW_SIZE = 5


black = Color(0x000000,1)
backround = RectangleAsset(WIDTH,HEIGHT,LineStyle(1,black),black)


Sprite(backround)
App().run()