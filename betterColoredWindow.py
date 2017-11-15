#Clay Kynor
#11/15/17
#betterColoredWindow.py

from random import randint
from ggame import *

def mouseClick(event):
    colors = [Color(0xff0000,1),Color(0x0000ff,1),Color(0x00ff00,1),Color(0xffff00,1)]
    num = randint(0,3)
    color = colors[num]
    line = LineStyle(3,color)
    rectangle = RectangleAsset(800,800,line,color)
    Sprite(rectangle)

App().listenMouseEvent("click",mouseClick)
App().run()