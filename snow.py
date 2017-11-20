#Clay Kynor
#11/20/17
#snow.py - making snow fall from the sky 

from ggame import *
from random import randint

WIDTH = 250
HEIGHT = 250
SNOW_SIZE = 5

def snow():
    #NEED TO ADD A LIBRARY THAT ADDS SNOWFLAKES

if __name__ == '__main__':

black = Color(0x000000,1)
white = Color(0xFFFFFF,1)
backround = RectangleAsset(WIDTH,HEIGHT,LineStyle(1,black),black)
snowFlake = CircleAsset(SNOW_SIZE,LineStyle(1,white),white)

Sprite(backround)
App().run(snow)